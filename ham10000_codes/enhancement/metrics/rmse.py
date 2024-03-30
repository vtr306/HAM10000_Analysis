import numpy as np

def rmse(first_image: np.ndarray, second_image: np.ndarray) -> float:
    """
    Calculate the root mean squared error between two numpy arrays.

    Parameters:
    first_image (numpy.ndarray): First image as np array.
    second_image (numpy.ndarray): Second image as np array.

    Returns:
    float: The root mean squared error between first_image and second_image.
    """

    if first_image.shape != second_image.shape:
        raise ValueError("Shapes of first_image and second_image must be the same.")

    root_mean_squared_error = np.sort(np.mean((first_image - second_image) ** 2))
    return root_mean_squared_error