from __future__ import print_function, division
import sys
import torch
import nibabel as nib
from torchvision.transforms import CenterCrop
from monai.visualize import GradCAM
from tqdm import tqdm
from tse_motion import get_densenet, get_unet, get_transfusion
import torchio as tio
import numpy as np
from torch.cuda.amp import autocast
from monai.networks.schedulers import DDIMScheduler

def rate(input_array, model=None, save_gradcam=False):
    if model is None:
        model = get_densenet()
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    
    ratings = []
    cam = GradCAM(nn_module=model, target_layers="class_layers.relu")
    transform = CenterCrop((512, 512))

    if isinstance(input_array, (nib.Nifti1Image, nib.Nifti2Image)):
        input_array = input_array.get_fdata()

    if len(input_array.shape) > 2:
        imgs = torch.tensor(input_array).permute(-1, 0, 1).to(device).float()
        imgs = torch.stack([img/img.max() for img in imgs])
        
        for img in tqdm(imgs):
            ratings.append(model(transform(img).unsqueeze(0).unsqueeze(0)).softmax(dim=1).argmax().detach().cpu())
        rating = torch.stack(ratings).float().mean()
        if save_gradcam:
            grad_cam = cam(x=imgs.unsqueeze(1))
            return rating.item(), grad_cam.squeeze()
    
    else:
        imgs = torch.tensor(input_array/input_array.max()).float().to(device)
        rating = model(transform(imgs).unsqueeze(0).unsqueeze(0)).softmax(dim=1).argmax().detach().cpu()
        if save_gradcam:
            grad_cam = cam(x=imgs.unsqueeze(0).unsqueeze(0))
            return rating.item(), grad_cam.squeeze()
    
    return rating.item()

def segment(tse, unet=None):
    if unet is None:
        unet = get_unet()
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    unet = unet.to(device)

    predictions = []

    if isinstance(tse, (nib.Nifti1Image, nib.Nifti2Image)):
        tse = tse.get_fdata()

    if len(tse.shape) > 2:
        height, width, _ = tse.shape
        subject_transform = CenterCrop((height, width))
        center_crop = tio.transforms.CropOrPad((512, 512, tse.shape[-1]))
        
        imgs = center_crop(np.expand_dims(tse, 0)).squeeze()
        imgs = torch.tensor((imgs/imgs.max())).permute(-1,0,1).to(device)
        for img in tqdm(imgs):
            prediction = unet(img.unsqueeze(0).unsqueeze(0).float())
            predictions.append(prediction)
        predictions = torch.stack(predictions)
        predictions = subject_transform(predictions.squeeze())
        return predictions.permute(1,2,3,0).detach().cpu()
    
    else:
        height, width = tse.shape
        subject_transform = CenterCrop((height, width))
        center_crop = tio.transforms.CropOrPad((512, 512, 1))
        
        tse = center_crop(np.expand_dims(np.expand_dims(tse,0),-1)).squeeze()
        prediction = unet(torch.tensor(tse/tse.max()).unsqueeze(0).unsqueeze(0).float().to(device)).squeeze().detach().cpu()
        
        return prediction

def set_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    if torch.backends.mps.is_available():
        torch.mps.manual_seed(seed)
    np.random.seed(seed)

def generate_fixed_noise(shape, seed, device):
    set_seed(seed)
    if device.type == 'mps':
        # MPS doesn't support torch.randn with generator, so we use CPU and transfer
        return torch.randn(shape, device='cpu').to(device)
    else:
        return torch.randn(shape, device=device)

def inference_batch(model, seed, scheduler, input_img, device, num_inference_steps=10, batch_size=12):
    model.eval()
    output_images = []
    
    for batch_start in tqdm(range(0, input_img.shape[0], batch_size)):
        batch_end = min(batch_start + batch_size, input_img.shape[0])
        batch_input = input_img[batch_start:batch_end].to(device).float()
        batch_input = torch.rot90(batch_input, 1, (2, 3))
        
        with torch.no_grad():
            
            noise = generate_fixed_noise(batch_input.shape, seed, device)
            current_img = noise
            combined = torch.cat((batch_input, noise), dim=1)
            
            scheduler.set_timesteps(num_inference_steps=num_inference_steps)
            # progress_bar = tqdm(scheduler.timesteps, desc=f"Processing batch {batch_start//batch_size + 1}")
            
            for t in scheduler.timesteps:
                with autocast(enabled=False):
                    model_output = model(combined, timesteps=torch.Tensor((t,)).to(current_img.device).repeat(combined.shape[0]))
                    current_img, _ = scheduler.step(model_output, t, current_img)
                    combined = torch.cat((batch_input, current_img), dim=1)
                    
            current_img = torch.rot90(current_img, -1, (2, 3))
            output_images.append(current_img.cpu())
    
    return torch.cat(output_images, dim=0).squeeze().permute(1,2,0)

def translate_t1(t1_img, num_seeds=3, num_inference_steps=10, scheduler=None):
    '''
    Translate T1 image to T2w TSE image using diffusion model.

    Usage:
        t1_img = torch.tensor(t1.get_fdata(), dtype=torch.float32).permute(-1,0,1).unsqueeze(1)
        t1_img = t1_img / t1_img.max()
        t1_img = t1_img.to(device)
        t2w_tse_img = translate_t1(t1_img, num_seeds=3, num_inference_steps=10)

    Args:
        t1_img (torch.Tensor): Normalized T1 image tensor on the appropriate device.
        num_seeds (int): Number of seeds for diffusion model. Default is 3.
        num_inference_steps (int): Number of inference steps for diffusion model. Default is 10.

    Returns:
        np.ndarray: T2w TSE image
    '''

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if scheduler is None:
        scheduler = DDIMScheduler(num_train_timesteps=1000)
    output_imgs = []
    model = get_transfusion()

    seeds = [33,38,53]
    num_seeds = min(num_seeds, len(seeds))
    for idx in range(num_seeds):
        
        seed = seeds[idx]
        output_img = inference_batch(model, seed, scheduler, t1_img, device, num_inference_steps, batch_size=1)
        output_imgs.append(output_img.numpy())

    output_imgs = np.stack(output_imgs).mean(0)

    return output_imgs

def main():
    if len(sys.argv) < 2:
        print("Usage: rate-motion <path_to_nifti_file>")
        sys.exit(1)
    input_path = sys.argv[1]
    try:
        input_data = nib.load(input_path)
    except Exception as e:
        print("Error loading file: {}".format(e))
        sys.exit(1)
    
    rating = rate(input_data)
    print('Input: {} | Motion Rating: {}'.format(input_path, rating))

if __name__ == '__main__':
    main()