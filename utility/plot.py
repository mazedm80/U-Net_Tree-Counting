import earthpy.plot as ep
import numpy as np
import matplotlib.pyplot as plt


def plot_image(images: np.ndarray, offset: int) -> None:
    """
    Plots 4 images from a given index.

    Args:
        images (np.ndarray): image array
        offset (int): start index
    """
    fig, ax = plt.subplots(ncols=4, nrows=1, figsize=(20, 4))
    for i in range(4):
        band_indices = [0, 1, 2]
        ep.plot_rgb(
            images[i*4+offset, :, :, :].transpose([2, 0, 1]),
            rgb=band_indices,
            title="False color composite image",
            stretch=True,
            ax=ax[i]
        )
    plt.show()


def plot_mask(mask: np.ndarray, offset: int) -> None:
    """
    Plots 4 mask from a given index.

    Args:
        mask (np.ndarray): mask array
        offset (int): start index
    """
    fig, ax = plt.subplots(ncols=4, nrows=1, figsize=(20, 4))
    for i in range(4):
        ax[i].imshow(mask[i*4+offset, :, :, :], cmap='binary')
        ax[i].set_title("Mask")
    plt.show()
