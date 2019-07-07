from pytorch_sound.models import register_model_architecture


@register_model_architecture('spectrogram_unet', 'spectrogram_unet_base')
def spec_unet_base():
    return {
        'spec_dim': 513,
        'hidden_dim': 256,
        'filter_len': 1024,
        'hop_len': 256,
        'layers': 4,
        'kernel_size': 5,
        'is_mask': True,
        'norm': 'ins'
    }