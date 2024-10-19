import torch
from tse_motion import get_transfusion, get_mp2rage_transfusion
import numpy as np
from tqdm import tqdm
from torch.cuda.amp import autocast
from monai.networks.schedulers import DDIMScheduler, DDPMScheduler
import nibabel as nib
import sys
import argparse

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

def translate_t1(t1_img, num_seeds=3, num_inference_steps=10, scheduler=None, is_mp2rage=False):
    '''
    Translate T1 image to T2w TSE image using diffusion model.

    Usage:
        t1_img = torch.tensor(t1.get_fdata(), dtype=torch.float32).permute(-1,0,1).unsqueeze(1)
        t1_img = t1_img / t1_img.max()
        t1_img = t1_img.to(device)
        t2w_tse_img = translate_t1(t1_img, num_seeds=3, num_inference_steps=10, is_mp2rage=False)

    Args:
        t1_img (torch.Tensor): Normalized T1 image tensor on the appropriate device.
        num_seeds (int): Number of seeds for diffusion model. Default is 3.
        num_inference_steps (int): Number of inference steps for diffusion model. Default is 10.
        scheduler (object): Scheduler for the diffusion process. If None, DDIMScheduler is used.
        is_mp2rage (bool): Whether the input is an MP2RAGE image. Default is False.

    Returns:
        np.ndarray: T2w TSE image
    '''

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if scheduler is None:
        scheduler = DDIMScheduler(num_train_timesteps=1000)
    output_imgs = []
    
    # Choose the appropriate model based on the is_mp2rage flag
    if is_mp2rage:
        model = get_mp2rage_transfusion()
    else:
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
    usage_example = """
    Example usage:
    translate-t1 -i input.nii.gz -o output.nii.gz -n 3 -s 20
    
    For MP2RAGE images:
    translate-t1 -i input_mp2rage.nii.gz -o output.nii.gz -n 3 -s 20 --mp2rage

    This will translate the T1 image 'input.nii.gz' (or MP2RAGE image 'input_mp2rage.nii.gz') 
    to a T2w TSE image 'output.nii.gz', using 3 seeds for averaging and 20 inference steps.
    """

    parser = argparse.ArgumentParser(
        description="Translate T1 image to T2w TSE image",
        epilog=usage_example,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-i', '--input', required=True, help="Path to input NIFTI file")
    parser.add_argument('-o', '--output', required=True, help="Path for output NIFTI file")
    parser.add_argument('-n', '--num_seeds', type=int, default=3, help="Number of seeds for diffusion model")
    parser.add_argument('-s', '--steps', type=int, default=10, help="Number of inference steps")
    parser.add_argument('-l', '--scheduler', type=str, default=None, help="DDIM or DDPM")
    parser.add_argument('--mp2rage', action='store_true', help="Use this flag if the input is an MP2RAGE image")
    args = parser.parse_args()

    if args.scheduler is not None:
        if args.scheduler == "DDPM":
            scheduler = DDPMScheduler(num_train_timesteps=1000)
            args.steps = 1000
        elif args.scheduler == "DDIM":
            scheduler = DDIMScheduler(num_train_timesteps=1000)
        else:
            raise ValueError(f"Scheduler {args.scheduler} not supported")
    else:
        scheduler = None

    t1 = nib.load(args.input)
    t1_img = torch.tensor(t1.get_fdata(), dtype=torch.float32).permute(-1,0,1).unsqueeze(1)
    t1_img = t1_img / t1_img.max()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    t1_img = t1_img.to(device)

    t2w_tse_img = translate_t1(t1_img, num_seeds=args.num_seeds, num_inference_steps=args.steps, 
                               scheduler=scheduler, is_mp2rage=args.mp2rage)
    t2w_tse = nib.Nifti1Image(t2w_tse_img, t1.affine, header=t1.header)
    t2w_tse.to_filename(args.output)

    print(f"Translated T2w TSE image saved to {args.output}")
    if args.mp2rage:
        print("MP2RAGE model was used for translation.")
    else:
        print("Standard T1 model was used for translation.")

if __name__ == "__main__":
    main()