import silicondiff_npu

_IS_DIFFUSERS_AVAILABLE = True
try:
    import diffusers
except ImportError:
    _IS_DIFFUSERS_AVAILABLE = False

if _IS_DIFFUSERS_AVAILABLE and hasattr(diffusers.models, "autoencoder_kl"):
    diffusers.models.autoencoder_kl.AutoencoderKL.blend_h = (
        silicondiff_npu.ops.tiled_vae_blend_h
    )
    diffusers.models.autoencoder_kl.AutoencoderKL.blend_v = (
        silicondiff_npu.ops.tiled_vae_blend_v
    )
