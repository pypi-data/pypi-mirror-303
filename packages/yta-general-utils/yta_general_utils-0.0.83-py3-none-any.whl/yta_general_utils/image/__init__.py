from yta_general_utils.file.checker import file_is_image_file
from yta_general_utils.file.filename import filename_is_type, FileType
from PIL import Image


# TODO: Apply types (str, Image.Image, etc.)
def parse_as_pillow_image(image):
    """
    Recognizes the provided 'image' as a Pillow Image and returns
    it if valid image  or image filename is provided.
    """
    if not image:
        raise Exception('No "image" parameter provided.')
    
    if isinstance(image, str):
        if not filename_is_type(image, FileType.IMAGE):
            raise Exception('The "image" parameter provided is not a valid image filename.')
        
        if not file_is_image_file(image):
            raise Exception('The "image" parameter provided is not a valid image.')
        
        image = Image.open(image)
    
    if not isinstance(image, Image.Image):
        raise Exception('The provided "image" parameter is not a Pillow image.')

    # TODO: How to know if numpy is an image (?) It is a numpy,
    # yes, but is it an image?
    # if isinstance(image, np.ndarray):
    # TODO: Check if it is not a valid numpy image or base64 image or
    # anything else that can be an Image
    return image
