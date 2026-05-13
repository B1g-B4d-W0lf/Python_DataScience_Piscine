import numpy as np
import matplotlib.pyplot as plt
import sys


def ft_invert(img: np.array) -> np.array:
    """Invert the colors on an image. """
    try:
        invert_img = img.copy()
        invert_img = 255 - invert_img

        plt.imshow(invert_img)
        plt.title("Inverted")
        plt.show()

    except Exception as e:
        print(f"Exeption :\n{e}\n Has been caught.")
        sys.exit(1)

    return invert_img


def ft_red(img: np.array) -> np.array:
    """Keeps only the red channel of an image"""
    try:
        red_img = img.copy()
        red_img[:, :, 1] = 0
        red_img[:, :, 2] = 0

        plt.imshow(red_img)
        plt.title("Red")
        plt.show()

    except Exception as e:
        print(f"Exeption :\n{e}\n Has been caught.")
        sys.exit(1)

    return red_img


def ft_green(img: np.array) -> np.array:
    """Keeps only the green channel of an image"""
    try:
        green_img = img.copy()
        green_img[:, :, 0] = 0
        green_img[:, :, 2] = 0

        plt.imshow(green_img)
        plt.title("Green")
        plt.show()

    except Exception as e:
        print(f"Exeption :\n{e}\n Has been caught.")
        sys.exit(1)

    return green_img


def ft_blue(img: np.array) -> np.array:
    """Keeps only the blue channel of an image"""
    try:
        blue_img = img.copy()
        blue_img[:, :, 0] = 0
        blue_img[:, :, 1] = 0

        plt.imshow(blue_img)
        plt.title("Blue")
        plt.show()

    except Exception as e:
        print(f"Exeption :\n{e}\n Has been caught.")
        sys.exit(1)

    return blue_img


def ft_grey(img: np.array) -> np.array:
    """Turns a colored image in shades of grey"""
    try:
        grey_img = img.copy()
        grey_img = np.dot(grey_img[..., :3], [0.2989, 0.5870, 0.1140])

        plt.imshow(grey_img, cmap=plt.get_cmap('gray'))
        plt.title("Grey")
        plt.show()

    except Exception as e:
        print(f"Exeption :\n{e}\n Has been caught.")
        sys.exit(1)

    return grey_img
