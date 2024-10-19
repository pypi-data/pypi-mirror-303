from yta_general_utils.image.region import PixelFilterFunction
from collections import Counter
from PIL import Image


def is_similar(color1, color2, tolerance: float = 30):
    if not tolerance:
        tolerance = 30

    return (abs(color1[0] - color2[0]) <= tolerance and
            abs(color1[1] - color2[1]) <= tolerance and
            abs(color1[2] - color2[2]) <= tolerance)

def _get_dominant_color(image_filename: str, pixel_filter_function: PixelFilterFunction = None):
    """
    Opens the provided 'image_filename' and gets the dominant
    color applying the 'filter_function' if provided.
    """
    img = Image.open(image_filename)
    img = img.convert('RGB')
    
    pixels = list(img.getdata())

    # Filter
    if pixel_filter_function is not None:
        pixels = [pixel for pixel in pixels if pixel_filter_function(pixel)]

    color_count = Counter(pixels)

    if pixel_filter_function is not None and not color_count:
        return None#, []
    
    dominant_color = color_count.most_common(1)[0][0] #[0][1] is the 'times'

    # Find similar colors (useful for making masks)
    #similar_colors = [color for color in color_count.keys() if is_similar(color, dominant_color, tolerance)]
    
    return dominant_color#, similar_colors

def get_most_common_rgb_color(image_filename):
    return _get_dominant_color(image_filename, PixelFilterFunction.is_green)