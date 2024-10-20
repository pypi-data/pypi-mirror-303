from PIL import Image
from io import BytesIO

import numpy as np
import base64


def base64_image_to_pil(base64_image):
    """
    Turns the 'base64_image' to a PIL Image, to be able
    to work with, and returns it.
    """
    return Image.open(BytesIO(base64.b64decode(base64_image)))

def base64_image_to_numpy(base64_image):
    """
    Turns the 'base64_image' to a numpy image (np.ndarray),
    to be able to work with, and returns it. 
    """
    return pil_image_to_numpy(base64_image_to_pil(base64_image))

def numpy_image_to_pil(numpy_image: np.ndarray):
    """
    Turns the 'numpy_image' ndarray to PIL readable image.
    """
    return Image.fromarray((numpy_image * 255).astype(np.uint8))

# TODO: How to set PIL type (?)
def pil_image_to_numpy(pil_image):
    """
    Turns the 'pil_image' to a numpy array. The PIL image must
    be an array produced by the code 'Image.open(image_filename)'.
    """
    return np.asarray(pil_image)
