from yta_general_utils.image.parser import ImageParser
from yta_multimedia.image.edition.resize import resize_image
from yta_multimedia.video.edition.resize import resize_video
from yta_multimedia.video.parser import VideoParser
from PIL import Image
from typing import Union

import numpy as np


class PixelFilterFunction:
    """
    Class to interact with image pixels and detect greens or transparent
    pixels to be used in, for example, ImageRegionFinder functionality.
    """
    @staticmethod
    def is_green(pixel):
        """
        This filter is the one we use to make sure it is a greenscreen
        color part by applying a [[0, r, 100], [100, g, 255], [0, b, 100]]
        filtering.
        """
        r, g, b = pixel

        return (r >= 0 and r <= 100) and (g >= 100 and g <= 255) and (b >= 0 and b <= 100)
    
    @staticmethod
    def is_transparent(pixel):
        """
        Checks if the alpha channel (4th in array) is set to 0 (transparent).
        The pixel must be obtained from a RGBA image (so 4 dimentions
        available).
        """
        _, _, _, a = pixel

        return a == 0

class Coordinate:
    """
    Class to represent a coordinate point (x, y).
    """
    x: int = None
    y: int = None

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Region:
    """
    Class to represent a region built by two coordinates, one in
    the top left corner and another one in the bottom right 
    corner.
    """
    top_left: Coordinate = None
    bottom_right: Coordinate = None
    _width: int = None
    _height: int = None

    def __init__(self, top_left_x: int, top_left_y: int, bottom_right_x: int, bottom_right_y: int):
        self.top_left = Coordinate(top_left_x, top_left_y)
        self.bottom_right = Coordinate(bottom_right_x, bottom_right_y)
        self._width = self.bottom_right.x - self.top_left.x
        self._height = self.bottom_right.y - self.top_left.y

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    def resize_image_to_fit_in(self, image):
        """
        This method rescales the provided 'image' to make it fit in
        this region. Once it's been rescaled, this image should be
        placed in the center of the region.
        """
        image = ImageParser.to_pillow(image)

        image = resize_image(image, (self.width, self.height))

        # We enlarge it by a 1% to avoid some balck pixels lines
        image = image.resize((image.size[0] * 1.01, image.size[1] * 1.01))

        return image

    # TODO: This could be private maybe
    def resize_video_to_fit_in(self, video):
        """
        This method rescales the provided 'video' to make it fit in
        this region. Once it's been rescaled, this video should be
        placed in the center of the region.
        """
        video = VideoParser.to_moviepy(video)

        video = resize_video(video, (self.width, self.height))

        # We enlarge it by a 1% to avoid some black pixels lines
        video = video.resize(1.01)

        return video
    
    def place_video_inside(self, video):
        """
        This method rescales the provided 'video' to make it fit in
        this region. Once it's been rescaled, this videos is 
        positioned in the required position to fit the region.
        """
        video = self.resize_video_to_fit_in(video)

        x = (self.bottom_right.x + self.top_left.x) / 2 - video.w / 2
        y = (self.bottom_right.y + self.top_left.y) / 2 - video.h / 2

        # TODO: What about upper limits (out of bottom left bounds) (?)
        if x < 0:
            x = 0
        if y < 0:
            y = 0

        video = video.set_position((x, y))

        return video

class ImageRegionFinder:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    @classmethod
    def is_valid(cls, x, y, image, visited, filter_func: callable):
        """
        This method verifies if the pixel is between the limits
        and is transparent and unvisited.
        """
        rows, cols, _ = image.shape

        return (0 <= x < rows and 0 <= y < cols and not visited[x, y] and filter_func(image[x, y]))

    @classmethod
    def dfs(cls, image: np.ndarray, visited, x, y, region, filter_func: callable):
        """
        A Deep First Search algorithm applied to the image to 
        obtain all the pixels connected in a region.
        """
        if not isinstance(image, np.ndarray):
            raise Exception('The provided "image" parameter is not a valid np.ndarray.')

        stack = [(x, y)]
        visited[x, y] = True
        region.append((x, y))
        
        while stack:
            cx, cy = stack.pop()
            for dx, dy in cls.directions:
                nx, ny = cx + dx, cy + dy
                if cls.is_valid(nx, ny, image, visited, filter_func):
                    visited[nx, ny] = True
                    region.append((nx, ny))
                    stack.append((nx, ny))

    @classmethod
    def is_inside(cls, small_bounds, large_bounds):
        """
        This method verifies if the bounds of a found region are
        inside another bounds to discard the smaller regions.
        """
        min_x_small, max_x_small, min_y_small, max_y_small = small_bounds
        min_x_large, max_x_large, min_y_large, max_y_large = large_bounds
        
        return (
            min_x_small >= min_x_large and max_x_small <= max_x_large and
            min_y_small >= min_y_large and max_y_small <= max_y_large
        )

    @classmethod
    def find_regions(cls, image: np.ndarray, filter_func: PixelFilterFunction) -> list[Region]:
        """
        This method looks for all the existing regions of transparent
        pixels that are connected ones to the others (neighbours). The
        'filter_func' parameter is the one that will classify the pixels
        as, for example, transparent or green. That 'filter_func' must
        be a method contained in the PixelFilterFunction class.

        This method returns the found regions as objects with 'top_left'
        and 'bottom_right' fields that are arrays of [x, y] positions
        corresponding to the corners of the found regions.
        """
        if not isinstance(image, np.ndarray):
            raise Exception('The provided "image" parameter is not a valid np.ndarray.')

        rows, cols, _ = image.shape
        visited = np.zeros((rows, cols), dtype=bool)
        regions = []
        
        for row in range(rows):
            for col in range(cols):
                # If we find a transparent pixel, we search
                if filter_func(image[row, col]) and not visited[row, col]:
                    region = []
                    cls.dfs(image, visited, row, col, region, filter_func)
                    
                    if region:
                        min_x = min(px[0] for px in region)
                        max_x = max(px[0] for px in region)
                        min_y = min(px[1] for px in region)
                        max_y = max(px[1] for px in region)
                        
                        # These are the limits of the region
                        bounds = (min_x, max_x, min_y, max_y)
                        
                        # We need to avoid small regions contained in others
                        if not any(cls.is_inside(bounds, r['bounds']) for r in regions):
                            regions.append({
                                # TODO: Maybe we need them to turn into transparent pixels
                                #'coordinates': region, # We don't need coordinates
                                'bounds': bounds
                            })

        # I want another format, so:
        for index, region in enumerate(regions):
            regions[index] = Region(region['bounds'][2], region['bounds'][0], region['bounds'][3], region['bounds'][1])
            # regions[index] = {
            #     # 'top_left': [region['bounds'][0], region['bounds'][2]],
            #     # 'bottom_right': [region['bounds'][1], region['bounds'][3]]
            #     # I don't know why I have to use it in this order but...
            #     'top_left': [region['bounds'][2], region['bounds'][0]],
            #     'bottom_right': [region['bounds'][3], region['bounds'][1]]
            # }

        return regions
    
    @classmethod
    def find_green_regions(cls, image: Union[str, Image.Image, np.ndarray]) -> list[Region]:
        """
        This method returns the found green regions as objects with
        'top_left' and 'bottom_right' fields that are arrays of [x, y] 
        positions corresponding to the corners of the found regions.
        """
        image = ImageParser.to_numpy(image, 'RGB')
            
        return cls.find_regions(image, PixelFilterFunction.is_green)
    
    @classmethod
    def find_transparent_regions(cls, image: Union[str, Image.Image, np.ndarray]) -> list[Region]:
        """
        This method returns the found transparent regions as objects
        with 'top_left' and 'bottom_right' fields that are arrays of
        [x, y] positions corresponding to the corners of the found
        regions.
        """
        image = ImageParser.to_numpy(image, 'RGBA')
            
        return cls.find_regions(image, PixelFilterFunction.is_transparent)