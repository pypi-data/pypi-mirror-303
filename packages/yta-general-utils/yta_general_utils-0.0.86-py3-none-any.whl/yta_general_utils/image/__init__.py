from yta_general_utils.file.checker import file_is_image_file
from yta_general_utils.file.filename import filename_is_type, FileType
from yta_general_utils.image.converter import numpy_image_to_pil, pil_image_to_numpy
from PIL import Image
from typing import Union

import numpy as np


class ImageParser:
    """
    Class to simplify the way we handle the image parameters
    so we can parse them as Pillow images, as numpy arrays,
    etc.
    """
    @classmethod
    def parse_as_pillow(cls, image: Union[str, Image.Image, np.ndarray]):
        """
        Returns an instance of a Pillow Image.Image of the given
        'image' if it is a valid image and no error found.
        """
        # TODO: By now we are only accepting string filenames,
        # Pillow Image.Image instances and numpy arrays.
        if not image:
            raise Exception('No "image" parameter provided.')
        
        if not isinstance(image, (str, Image.Image, np.ndarray)):
            raise Exception('The "image" parameter provided is not a string nor a Image.Image nor a np.ndarray.')

        # We can have problems with np.ndarray
        if isinstance(image, np.ndarray):
            image = numpy_image_to_pil(image)
        elif isinstance(image, str):
            if not filename_is_type(image, FileType.IMAGE):
                raise Exception('The "image" parameter provided is not a valid image filename.')
            
            if not file_is_image_file(image):
                raise Exception('The "image" parameter provided is not a valid image.')
            
            image = Image.open(image)

        return image
    
    @classmethod
    def parse_as_numpy(cls, image: Union[str, Image.Image, np.ndarray], mode: str = 'RGB'):
        """
        Returns a numpy array representing the given 'image'
        if it is a valid image and no error found.

        The 'mode' parameter will be used to open the image
        with Pillow library and then turning into numpy when
        necessary. Must be 'RGB' or 'RGBA'.
        """
        # TODO: By now we are only accepting string filenames,
        # Pillow Image.Image instances and numpy arrays.
        if not image:
            raise Exception('No "image" parameter provided.')
        
        if not isinstance(image, (str, Image.Image, np.ndarray)):
            raise Exception('The "image" parameter provided is not a string nor a Image.Image nor a np.ndarray.')
        
        if not mode:
            mode = 'RGB'

        if mode not in ['RGB', 'RGBA']:
            raise Exception('The provided "mode" parameters is not a valid mode: RGB or RGBA.')

        # We can have problems with np.ndarray
        if isinstance(image, Image.Image):
            image = pil_image_to_numpy(image)
        elif isinstance(image, str):
            if not filename_is_type(image, FileType.IMAGE):
                raise Exception('The "image" parameter provided is not a valid image filename.')
            
            if not file_is_image_file(image):
                raise Exception('The "image" parameter provided is not a valid image.')
            
            image = pil_image_to_numpy(Image.open(image).convert(mode))

        return image