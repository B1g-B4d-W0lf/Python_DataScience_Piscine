from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
import sys
import os


def rgbtogray(rgb) -> np.array:
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def ft_zoom(img) -> np.array:
    h, w = img.shape
    zh, zw = 400, 400
    eh = round((h - zh) // 2)
    ew = round((w - zw) // 2)

    z_img = img[eh:eh + zh, ew:ew + zw]
    return (z_img)


def ft_transpose(img) -> np.array:
    h, w = img.shape
    dest = np.zeros((w, h), dtype=img.dtype)

    for i in range(h):
        for j in range(w):
            new_line = (w - 1) - j
            new_col = i
            dest[new_line, new_col] = img[i, j]
    return (dest)


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Use is: 'rotate.py [img path]'")
        target = sys.argv[1]
        if not target.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("Only 'jpg' or 'jpeg' format supported.")
        if not os.path.exists(target):
            raise AssertionError("File does not exist / \
                is in the wrong directory.")

        target = ft_load(target)
        print(target)
        img = rgbtogray(target)
        z_img = ft_zoom(img)
        t_img = ft_transpose(z_img)

        print(f"New shape after transpose: {t_img.shape}")
        print(t_img)

        plt.imshow(t_img, cmap=plt.get_cmap('gray'))
        plt.show()

    except AssertionError as e:
        print(e)
        sys.exit(1)

    except Exception as e:
        print(f"Exception : {e} has been caught")
        sys.exit(1)


if __name__ == "__main__":
    main()
