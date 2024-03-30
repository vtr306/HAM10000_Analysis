import numpy as np
from skimage.restoration import denoise_tv_chambolle

def total_variation(image: np.ndarray, weight: float = 0.1) -> np.ndarray:
    """
    Denoise an image using total variation (TV) denoising with the Chambolle algorithm.

    Parameters:
    image (numpy.ndarray): The input image.
    weight (float): The regularization parameter.

    Returns:
    numpy.ndarray: The denoised image.
    """
    # Apply total variation denoising
    denoised_image = denoise_tv_chambolle(image, weight=weight)
    return denoised_image