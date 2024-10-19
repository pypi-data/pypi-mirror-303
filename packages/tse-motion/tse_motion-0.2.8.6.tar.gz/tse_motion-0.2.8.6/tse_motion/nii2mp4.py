import nibabel as nib
import numpy as np
import cv2
import argparse
from tqdm import tqdm

def normalize_slice(slice):
    """Normalize the slice to 0-255 range for video encoding."""
    slice_min, slice_max = slice.min(), slice.max()
    return ((slice - slice_min) / (slice_max - slice_min) * 255).astype(np.uint8)

def nii_to_mp4(input_file, output_file, axis=2, fps=10):
    """
    Convert a NIfTI file to MP4 video.
    
    Args:
    input_file (str): Path to the input NIfTI file.
    output_file (str): Path to the output MP4 file.
    axis (int): Axis along which to create video slices (0, 1, or 2). Default is 2.
    fps (int): Frames per second for the output video. Default is 10.
    """
    # Load the NIfTI file
    nii_img = nib.load(input_file)
    data = nii_img.get_fdata()

    # Determine the shape and size of the output video
    if axis == 0:
        num_slices, height, width = data.shape
    elif axis == 1:
        height, num_slices, width = data.shape
    else:  # axis == 2
        height, width, num_slices = data.shape

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    # Write each slice as a frame
    for i in tqdm(range(num_slices), desc="Creating video"):
        if axis == 0:
            slice = data[i, :, :]
        elif axis == 1:
            slice = data[:, i, :]
        else:  # axis == 2
            slice = data[:, :, i]
        
        # Normalize and convert to RGB
        frame = normalize_slice(slice)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        
        # Write the frame
        out.write(frame_rgb)

    # Release the VideoWriter
    out.release()

    print(f"Video saved as {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Convert NIfTI file to MP4 video")
    parser.add_argument('-i', '--input', required=True, help="Path to input NIFTI file")
    parser.add_argument('-o', '--output', required=True, help="Path for output NIFTI file")
    parser.add_argument("-a", "--axis", type=int, choices=[0, 1, 2], default=2,
                        help="Axis along which to create video slices (0, 1, or 2). Default is 2.")
    parser.add_argument("-f", "--fps", type=int, default=10,
                        help="Frames per second for the output video. Default is 10.")
    
    args = parser.parse_args()

    nii_to_mp4(args.input, args.output, args.axis, args.fps)

if __name__ == "__main__":
    main()