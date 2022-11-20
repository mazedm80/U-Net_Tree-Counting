from pathlib import Path
from typing import Tuple

import numpy as np
import rasterio as rs


def image_to_nparray(image_path: Path, mask_path: Path, band_no: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Takes image path and mask path and convert them into numpy array.

    Args:
        image_path (Path): Image path.
        mask_path (Path): Mask path.
        band_no (int): number of image band.

    Returns:
        Tuple[np.ndarray, np.ndarray]: returns both the image and mask as numpy array.
    """
    with rs.open(image_path) as img:
        image = img.read(list(range(1, band_no + 1)))
        image_rgba = np.array(image, dtype=np.float32)
        imgage_array = np.moveaxis(image_rgba, 0, -1)
    with rs.open(mask_path) as mask:
        mask_array = np.array(mask.read([1]))
        mask_array = np.moveaxis(mask_array, 0, -1)
    return imgage_array, mask_array


def image_transformation(image: np.ndarray, mask: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """
    Apply random transformation to the image and mask.

    Args:
        image (np.ndarray): image array.
        mask (np.ndarray): mask array.

    Returns:
        Tuple[np.ndarray, np.ndarray]: returns both the image and mask as numpy array.
    """
    image_list = []
    mask_list = []
    image_list.append(image)
    mask_list.append(mask)
    rt = np.random.randint(1, 2)
    if rt == 1:
        # reverse first dimension
        image_transform = image[::-1, :, :]
        mask_transform = mask[::-1, :, :]
        image_list.append(image_transform)
        mask_list.append(mask_transform)
        # interchange first and second dimensions
        image_transform = image.transpose([1, 0, 2])
        mask_transform = mask.transpose([1, 0, 2])
        image_list.append(image_transform)
        mask_list.append(mask_transform)
        # rotate 90 twice
        image_transform = np.rot90(image, 2)
        mask_transform = np.rot90(mask, 2)
        image_list.append(image_transform)
        mask_list.append(mask_transform)

    else:
        # reverse second dimension
        image_transform = image[:, ::-1, :]
        mask_transform = image[:, ::-1, :]
        image_list.append(image_transform)
        mask_list.append(mask_transform)
        # rotate 90 once
        image_transform = np.rot90(image, 1)
        mask_transform = np.rot90(mask, 1)
        image_list.append(image_transform)
        mask_list.append(mask_transform)
        # rotate 90 three times
        image_transform = np.rot90(image, 3)
        mask_transform = np.rot90(mask, 3)
        image_list.append(image_transform)
        mask_list.append(mask_transform)
    # return as numpy array
    return np.array(image_list), np.array(mask_list)


def class_percentage(mask: np.ndarray) -> float:
    """
    Calculates the tree pixel percentage in a mask.

    Args:
        mask (np.ndarray): mask.

    Returns:
        float: the percentage value.
    """
    count = 0
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if (mask[i, j, 0] == 1):
                count += 1
            else:
                continue
    return ((count * 100)/(mask.shape[0] * mask.shape[1]))


def extract_patches(
        images: np.ndarray,
        masks: np.ndarray,
        min_limit: float,
        max_limit: float
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generates image and mask patches based on given minimum and maximum tree cover percntage.

    Args:
        images (np.ndarray): image array.
        masks (np.ndarray): mask array.
        min_limit (float): minimum tree cover.
        max_limit (float): maximum tree cover.

    Returns:
        Tuple[np.ndarray, np.ndarray]: returns both the image and mask as numpy array.
    """
    index = 1
    image_list = []
    mask_list = []
    for i in range(images.shape[0]):
        for j in range(images.shape[1]):
            image = images[i, j, 0, :, :, :]
            mask = masks[i, j, 0, :, :, :]
            if (class_percentage(mask) >= min_limit and class_percentage(mask) <= max_limit):
                image_transform, mask_transform = image_transformation(image, mask)
                for k in range(image_transform.shape[0]):
                    image_list.append(image_transform[k, :, :, :])
                    mask_list.append(mask_transform[k, :, :, :])
                    index += 1
            else:
                continue
    print("The number of image chips generated is: ", index)
    return np.array(image_list), np.array(mask_list)
