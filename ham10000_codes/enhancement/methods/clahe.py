import cv2
import numpy as np

def clahe(image: np.ndarray, clip_limit: float = 2.0, tile_grid_size: tuple = (8, 8)) -> np.ndarray:
    """
    Apply Contrast Limited Adaptive Histogram Equalization (CLAHE) to an input image.

    Parameters:
    image (numpy.ndarray): The input image.
    clip_limit (float): Threshold for contrast limiting.
    tile_grid_size (tuple): Size of grid for histogram equalization.

    Returns:
    numpy.ndarray: The contrast enhanced image.
    """
    # Check if the image is grayscale
    if len(image.shape) != 2:
        raise ValueError("Input image must be grayscale.")
    
    # If the image is grayscale, apply CLAHE directly
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    clahe_image = clahe.apply(image)
    return clahe_image