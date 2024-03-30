import numpy as np
import cv2

def absolute_mean_brightness_error(first_image: np.ndarray, second_image: np.ndarray) -> float:
    """
    Calculate the Absolute Mean Brightness Error between two images.

    Parameters:
    first_image (numpy.ndarray): The first image.
    second_image (numpy.ndarray): The second image.

    Returns:
    float: The Absolute Mean Brightness Error between first_image and second_image.
    """
    # Check if both images have the same shape
    if first_image.shape != second_image.shape:
        raise ValueError("Shapes of first_image and second_image must be the same.")

    # Check if both images are in grayscale
    if ((len(first_image.shape) != 2) or (len(second_image.shape) != 2)):
        raise ValueError("Input images must be grayscale.")


    # Calculate the absolute mean brightness error
    ambe = np.mean(np.abs(first_image - second_image))
    return ambe