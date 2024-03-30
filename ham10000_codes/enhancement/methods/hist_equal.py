import cv2
import numpy as np

def hist_equal(image: np.ndarray) -> np.ndarray:
    """
    Apply histogram equalization to an input grayscale image.

    Parameters:
    image (numpy.ndarray): The input grayscale image.

    Returns:
    numpy.ndarray: The histogram equalized image.
    """
    # Check if the image is grayscale
    # if len(image.shape) != 2:
    #     raise ValueError("Input image must be grayscale.")

    # Apply histogram equalization
    equalized_image = cv2.equalizeHist(image)
    return equalized_image
