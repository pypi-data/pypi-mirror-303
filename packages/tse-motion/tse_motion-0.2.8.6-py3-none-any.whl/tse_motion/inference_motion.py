import torch
from tse_motion import get_tse_ma
import numpy as np
from tqdm import tqdm
from torch.cuda.amp import autocast
import nibabel as nib
import argparse

def calculate_nrmse(diff_map):
    """
    Calculate the normalized root mean square error (NRMSE) between the difference map and a zero array.
    The result is normalized to be between 0 and 1.
    """
    mse = np.mean(np.square(diff_map))
    rmse = np.sqrt(mse)
    nrmse = rmse / (np.max(diff_map) - np.min(diff_map))
    return nrmse

def inference_batch(model, input_img, device, batch_size=12, is_nifti=False):
    model.eval()
    output_images = []
    
    for batch_start in tqdm(range(0, input_img.shape[0], batch_size)):
        batch_end = min(batch_start + batch_size, input_img.shape[0])
        batch_input = input_img[batch_start:batch_end].to(device).float()
        
        if is_nifti:
            batch_input = torch.rot90(batch_input, 1, (2, 3))
        
        with torch.no_grad():
            with autocast(enabled=False):
                model_output, _, _ = model(batch_input)
                    
            if is_nifti:
                model_output = torch.rot90(model_output, -1, (2, 3))
            
            output_images.append(model_output.cpu())
    
    return torch.cat(output_images, dim=0).squeeze().permute(1,2,0)

def reconstruct(input_data, device, is_nifti=False, batch_size=12):
    model = get_tse_ma()
    model.to(device)
    
    # Ensure input_data is a 4D tensor (batch, channel, height, width)
    if isinstance(input_data, np.ndarray):
        input_data = torch.from_numpy(input_data)
    
    if input_data.dim() == 3:
        input_data = input_data.unsqueeze(1)
    
    # Normalize input image
    input_data = input_data / input_data.max()
    
    # Perform reconstruction
    reconstructed_img = inference_batch(model, input_data, device, batch_size=batch_size, is_nifti=is_nifti)
    
    return reconstructed_img


def main():
    parser = argparse.ArgumentParser(
        description="Reconstruct image using AutoencoderKL and compute difference",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('-i', '--input', required=True, help="Path to input NIFTI file")
    parser.add_argument('-o', '--output', required=True, help="Path for output NIFTI file")
    parser.add_argument('-b', '--batch_size', type=int, default=12, help="Batch size for inference (default: 12)")
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load input image
    input_nifti = nib.load(args.input)
    input_data = input_nifti.get_fdata()
    input_tensor = torch.tensor(input_data, dtype=torch.float32).permute(-1, 0, 1)

    # Perform reconstruction
    reconstructed_img = reconstruct(input_tensor, device, is_nifti=True, batch_size=args.batch_size)

    # Convert back to numpy
    reconstructed_data = reconstructed_img.numpy()
   
    # Create NIFTI images
    reconstructed_nifti = nib.Nifti1Image(reconstructed_data, input_nifti.affine, header=input_nifti.header)
    
    # Save output
    nib.save(reconstructed_nifti, args.output)
    
    print(f"Reconstructed image saved to {args.output}")

if __name__ == "__main__":
    main()