import os
import numpy as np
import torch
import nibabel as nib
import cv2
from tqdm import tqdm
from sam2.sam2_video_predictor import SAM2VideoPredictor
import argparse
import pdb

class SAM2NiftiPredictor:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.predictor = SAM2VideoPredictor.from_pretrained("facebook/sam2-hiera-large")
        self.inference_state = None
        self.original_nifti = None

    def nifti_to_mp4(self, nifti_path, output_path, fps=10):
        self.original_nifti = nib.load(nifti_path)
        nifti_data = self.original_nifti.get_fdata()
        nifti_data = ((nifti_data - nifti_data.min()) / (nifti_data.max() - nifti_data.min()) * 255).astype(np.uint8)
        height, width, num_frames = nifti_data.shape
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        for i in range(num_frames):
            frame = nifti_data[:, :, i]
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
            out.write(frame_rgb)
        out.release()
        return output_path

    def init_state(self, video_path):
        self.inference_state = self.predictor.init_state(video_path=video_path)

    def add_points(self, frame_idx, obj_id, points, labels):
        _, out_obj_ids, out_mask_logits = self.predictor.add_new_points_or_box(
            inference_state=self.inference_state,
            frame_idx=frame_idx,
            obj_id=obj_id,
            points=points,
            labels=labels,
        )
        return out_obj_ids, out_mask_logits

    def propagate(self):
        video_segments = {}
        for out_frame_idx, out_obj_ids, out_mask_logits in self.predictor.propagate_in_video(self.inference_state):
            video_segments[out_frame_idx] = {
                out_obj_id: (out_mask_logits[i] <= 0.0).cpu().numpy()  # Invert the condition here
                for i, out_obj_id in enumerate(out_obj_ids)
            }
        return video_segments

    def save_segmentation_as_nifti(self, video_segments, output_path):
        if self.original_nifti is None:
            raise ValueError("Original NIfTI data not loaded. Please run nifti_to_mp4() first.")
        original_shape = self.original_nifti.shape
        segmentation_data = np.ones(original_shape, dtype=np.uint8)  # Initialize with ones instead of zeros
        for frame_idx, obj_dict in video_segments.items():
            for obj_id, mask in obj_dict.items():
                segmentation_data[:, :, frame_idx] = mask.astype(np.uint8)
        segmentation_nifti = nib.Nifti1Image(segmentation_data, self.original_nifti.affine, self.original_nifti.header)
        image_data = segmentation_data * self.original_nifti.get_fdata()
        image_data_nifti = nib.Nifti1Image(image_data, self.original_nifti.affine, self.original_nifti.header)
        nib.save(segmentation_nifti, output_path)
        nib.save(image_data_nifti, output_path.replace('headmask', 'carvedhead'))


def remove_background_nifti(input_path, output_path):
    nifti_predictor = SAM2NiftiPredictor()
    
    # Convert NIfTI to MP4
    mp4_path = input_path.replace('.nii.gz', '.mp4')
    nifti_predictor.nifti_to_mp4(input_path, mp4_path)
    
    # Initialize SAM2 state
    nifti_predictor.init_state(mp4_path)
    row, col = nib.load(input_path).shape[:-1]
    # Add points for segmentation (example coordinates, adjust as needed)
    frame_idx = 0
    obj_id = 1
    points = np.array([[1, 1], [row, col], [1, col], [row, 1]], dtype=np.float32)
    labels = np.array([1, 1, 1, 1], dtype=np.int32)
    nifti_predictor.add_points(frame_idx, obj_id, points, labels)
    
    # Propagate segmentation
    video_segments = nifti_predictor.propagate()
    # Save segmentation as NIfTI
    nifti_predictor.save_segmentation_as_nifti(video_segments, output_path)
    
    # Clean up temporary MP4 file
    os.remove(mp4_path)

def main():
    parser = argparse.ArgumentParser(description="Remove background from NIFTI image using SAM2")
    parser.add_argument('-i', '--input', required=True, help="Path to input NIFTI file")
    parser.add_argument('-o', '--output', required=True, help="Path for output NIFTI file")
    args = parser.parse_args()

    remove_background_nifti(args.input, args.output)

if __name__ == "__main__":
    main()