from yta_general_utils.image.region import PixelFilterFunction
from collections import Counter
from PIL import Image


def get_most_common_green_rgb_color(image_filename):
    """
    Returns the most common (dominant) rgb color in a 
    (r, g, b) format.
    """
    return get_dominant_color(image_filename, PixelFilterFunction.is_green)

def get_most_common_green_rgb_color_and_similars(image_filename):
    """
    Returns the most common rgb color and its similar colors
    found in the provided 'image_filename' as a pair of values
    (most_common, similars). Extract them as a pair.
    """
    return get_dominant_and_similar_colors(image_filename, PixelFilterFunction.is_green, _is_similar_green)

def get_dominant_color(image_filename: str, pixel_filter_function: PixelFilterFunction = None):
    """
    Opens the provided 'image_filename' and gets the dominant
    color applying the 'pixel_filter_function' if provided.
    """
    dominant, _ = _get_dominant_color(image_filename, pixel_filter_function)

    return dominant

def get_dominant_and_similar_colors(image_filename: str, pixel_filter_function: PixelFilterFunction = None, similarity_function = None):
    """
    Opens the provided 'image_filename', gets the dominant
    color and also the similar ones by applying the 
    'pixel_filter_function' if provided.
    """
    return _get_dominant_color(image_filename, pixel_filter_function, similarity_function)

def _is_similar_green(color1, color2, tolerance: float = 30):
    if not tolerance:
        tolerance = 30

    # TODO: This below should be comparing 
    return (abs(color1[0] - color2[0]) <= tolerance * 0.5 and
            abs(color1[1] - color2[1]) <= tolerance * 2 and
            abs(color1[2] - color2[2]) <= tolerance * 0.5)

def _get_dominant_color(image_filename: str, pixel_filter_function: PixelFilterFunction = None, similarity_function = None):
    img = Image.open(image_filename).convert('RGB')
    
    pixels = list(img.getdata())
    if pixel_filter_function is not None:
        pixels = [pixel for pixel in pixels if pixel_filter_function(pixel)]

    color_count = Counter(pixels)

    if not color_count:
        return None, None

    dominant_color = color_count.most_common(1)[0][0] #[0][1] is the 'times'

    if similarity_function is None:
        return dominant_color, None

    similar_colors = [color for color in color_count.keys() if similarity_function(color, dominant_color, 30) and color != dominant_color]
    
    return dominant_color, similar_colors