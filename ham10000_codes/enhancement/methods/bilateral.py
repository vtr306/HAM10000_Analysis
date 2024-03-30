import cv2
import numpy as np

def bilateral(image: np.ndarray, d: int = 9, sigma_color: float = 75, sigma_space: float = 75) -> np.ndarray:
    """
    Apply bilateral filter to an input image.

    Parameters:
    image (numpy.ndarray): The input image.
    d (int): Diameter of each pixel neighborhood.
    sigma_color (float): Filter sigma in the color space.
    sigma_space (float): Filter sigma in the coordinate space.

    Returns:
    numpy.ndarray: The filtered image.
    """
    # Check if the image is grayscale
    if len(image.shape) != 2:
        raise ValueError("Input image must be grayscale.")

    filtered_image = cv2.bilateralFilter(image, d, sigma_color, sigma_space)
    
    return filtered_image
