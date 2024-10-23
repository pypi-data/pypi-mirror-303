from PIL import Image
from io import BytesIO

import numpy as np
import base64


def base64_image_to_pil(base64_image):
    """
    Turns the 'base64_image' to a PIL Image, to be able
    to work with, and returns it.
    """
    # TODO: Check that 'base64_image' is a base64 image
    return Image.open(BytesIO(base64.b64decode(base64_image)))

def base64_image_to_numpy(base64_image):
    """
    Turns the 'base64_image' to a numpy image (np.ndarray),
    to be able to work with, and returns it. 
    """
    # TODO: Check that 'base64_image' is a base64 image
    return pil_image_to_numpy(base64_image_to_pil(base64_image))

def numpy_image_to_pil(numpy_image: np.ndarray):
    """
    Turns the 'numpy_image' ndarray to PIL readable image.
    """
    if not isinstance(numpy_image, np.ndarray):
        raise Exception('The provided "numpy_image" parameter is not a numpy np.ndarray instance.')

    return Image.fromarray((numpy_image * 255).astype(np.uint8))

def pil_image_to_numpy(pil_image: Image.Image):
    """
    Turns the 'pil_image' to a numpy array. The PIL image must
    be an array produced by the code 'Image.open(image_filename)'.
    """
    if not isinstance(pil_image, Image.Image):
        raise Exception('The provided "pil_image" parameter is not a Pillow Image instance.')

    return np.asarray(pil_image)
