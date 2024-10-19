import torch
from monai.networks.nets import DenseNet121
from pkg_resources import resource_filename
from .unet import UNet
from monai.networks.nets import DiffusionModelUNet
from generative.networks.nets import AutoencoderKL
from huggingface_hub import hf_hub_download


def get_densenet(device=None):
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    model = DenseNet121(spatial_dims=2, in_channels=1, out_channels=5)
    model_path = resource_filename('tse_motion', 'weight.pth')
    
    try:
        model.load_state_dict(torch.load(model_path, map_location=device))
    except Exception as e:
        raise RuntimeError(f"Failed to load DenseNet model: {e}")
    
    return model.to(device).eval()

def get_unet(device=None):
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    unet = UNet(in_channels=1, out_channels=2, init_features=32)
    unet_path = hf_hub_download(repo_id='jil202/tse_motion', filename="unet-checkpoint.pth")
    
    try:
        unet.load_state_dict(torch.load(unet_path, map_location=device))
    except Exception as e:
        raise RuntimeError(f"Failed to load UNet model: {e}")
    
    return unet.to(device).eval()

def get_transfusion(device=None):
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = DiffusionModelUNet(
        spatial_dims=2,
        in_channels=2,  # T1w + noise
        out_channels=1,  # TSE
        channels=(256, 256, 512),
        attention_levels=(False, False, True),
        num_res_blocks=2,
        num_head_channels=512,
        with_conditioning=False,
    )

    model_path = hf_hub_download(repo_id='jil202/tse_motion', filename="t1_to_tse.pt")

    try:
        model.load_state_dict(torch.load(model_path, map_location=device))
    except Exception as e:
        raise RuntimeError(f"Failed to load UNet model: {e}")
    
    return model.to(device).eval()

def get_mp2rage_transfusion(device=None):
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = DiffusionModelUNet(
        spatial_dims=2,
        in_channels=2,  # T1w + noise
        out_channels=1,  # TSE
        channels=(256, 256, 512),
        attention_levels=(False, False, True),
        num_res_blocks=2,
        num_head_channels=512,
        with_conditioning=False,
    )

    model_path = hf_hub_download(repo_id='jil202/tse_motion', filename="mp2rage-tse.pt")

    try:
        model.load_state_dict(torch.load(model_path, map_location=device))
    except Exception as e:
        raise RuntimeError(f"Failed to load UNet model: {e}")
    
    return model.to(device).eval()


def get_aekl(device=None):
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = AutoencoderKL(
        spatial_dims=2,
        in_channels=1,  # T1w + noise
        out_channels=1,  # TSE
        num_channels=(128, 256, 256, 512),
        attention_levels=(False, False, False, False),
        latent_channels=3,
        num_res_blocks=2,
        with_encoder_nonlocal_attn=False,
        with_decoder_nonlocal_attn=False
    )

    model_path = hf_hub_download(repo_id='jil202/tse_motion', filename="tse_aekl.pt")

    try:
        model.load_state_dict(torch.load(model_path, map_location=device))
    except Exception as e:
        raise RuntimeError(f"Failed to load UNet model: {e}")
    
    return model.to(device).eval()