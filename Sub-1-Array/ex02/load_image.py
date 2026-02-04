import numpy as np
from PIL import Image

def ft_load(path: str) -> np.array:
    try:
        image = Image.open(path)
        image_array = np.array(image)
        print(f'The shape of the image is: {image_array.shape}')
        return image_array

    except Exception as e:
        print(f"Exception : {e} has been caught")
        exit()
    return None