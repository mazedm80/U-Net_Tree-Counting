import cv2
import numpy as np
from skimage import filters


def Gaussian_filter(image: np.ndarray, sigma: int = 1) -> np.ndarray:
    """Apply Gaussian filter to an image.

    Args:
        image (np.ndarray): The image as a numpy array.
        sigma (int, optional): Gaussian kernel. Defaults to 1.

    Returns:
        np.ndarray: The image as a numpy array.
    """
    image = np.copy(image)
    blur = filters.gaussian(image, sigma=sigma)
    return blur


def Find_threshold_otsu(image: np.ndarray) -> float:
    """Find the otsu thereshold of an image.

    Args:
        image (np.ndarray): The image as a numpy array.

    Returns:
        float: The otsu threshold value.
    """
    t = filters.threshold_otsu(image)
    return t


def Binary(image: np.ndarray, threshold: float, max_value: int = 1) -> np.ndarray:
    """Apply binary threshold to an image.

    Args:
        image (np.ndarray): The image as a numpy array.
        threshold (float): The otsu threshold value.
        max_value (int, optional): The maximum pixel value of the output image. Defaults to 1.

    Returns:
        np.ndarray: The binary image.
    """
    imaeg = np.copy(image)
    (t, masklayer) = cv2.threshold(image, threshold, max_value, cv2.THRESH_BINARY)
    return masklayer
