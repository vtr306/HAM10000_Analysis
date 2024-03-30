import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def calculate_ssim(first_image: np.ndarray, second_image: np.ndarray) -> float:
    """
    Calculate the Structural Similarity Index (SSIM) between two images.

    Parameters:
    first_image (numpy.ndarray): The first image.
    second_image (numpy.ndarray): The second image.

    Returns:
    float: The SSIM between the two images.
    """
    # Check if both images have the same shape
    if first_image.shape != second_image.shape:
        raise ValueError("Shapes of first_image and second_image must be the same.")

    # Convert images to grayscale using OpenCV
    if len(first_image.shape) == 3:
        first_image = cv2.cvtColor(first_image, cv2.COLOR_RGB2GRAY)
    if len(second_image.shape) == 3:
        second_image = cv2.cvtColor(second_image, cv2.COLOR_RGB2GRAY)

    # Calculate SSIM
    ssim_value = ssim(first_image, second_image, data_range=first_image.max() - first_image.min())
    return ssim_value
