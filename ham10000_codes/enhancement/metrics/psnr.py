import numpy as np

def psnr(first_image: np.ndarray, second_image: np.ndarray) -> float:
    """
    Calculate the Peak Signal-to-Noise Ratio (PSNR) between two images.

    Parameters:
    first_image (numpy.ndarray): The first image.
    second_image (numpy.ndarray): The second image.

    Returns:
    float: The PSNR between the first and second images.
    """
    # Check if both images have the same shape
    if first_image.shape != second_image.shape:
        raise ValueError("Shapes of first_image and second_image must be the same.")
    
    # Calculate max pixel
    max_pixel = 255

    # Calculate the mean squared error
    mse = np.mean((first_image - second_image) ** 2)

    # Calculate PSNR
    if mse == 0:
        return float('inf')
    psnr_value = 10 * np.log10((max_pixel**2) / mse)
    return psnr_value

