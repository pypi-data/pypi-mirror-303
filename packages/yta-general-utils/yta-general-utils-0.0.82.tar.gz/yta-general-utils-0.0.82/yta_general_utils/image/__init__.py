from yta_general_utils.image.checker import is_valid_image
from yta_general_utils.file.filename import filename_is_type, FileType
from PIL import Image


# TODO: Apply types (str, Image.Image, etc.)
def recognize_image(image):
    """
    Recognizes the provided 'image' as an Image and returns it as
    it is or as a PIL Image if valid image filename is provided.
    """
    if not image:
        raise Exception('No "image" provided.')
    
    if isinstance(image, str):
        if not filename_is_type(image, FileType.IMAGE):
            raise Exception('The "image" parameter is not a valid image filename.')

        if not is_valid_image(image):
            raise Exception('The "image" parameter provided is not a valid image.')
        
        image = Image.open(image)

    # TODO: How to know if numpy is an image (?) It is a numpy,
    # yes, but is it an image?
    # if isinstance(image, np.ndarray):
    # TODO: Check if it is not a valid numpy image or base64 image or
    # anything else that can be an Image
    return image
