from yta_general_utils.image.region import PixelFilterFunction
from collections import Counter
from PIL import Image


def is_similar(color1, color2, tolerance: float = 30):
    if not tolerance:
        tolerance = 30

    return (abs(color1[0] - color2[0]) <= tolerance and
            abs(color1[1] - color2[1]) <= tolerance and
            abs(color1[2] - color2[2]) <= tolerance)

def _get_dominant_color(image_filename: str, color_filter_function: PixelFilterFunction = None):
    """
    Opens the provided 'image_filename' and gets the dominant
    color applying the 'color_filter_function' if provided.
    """
    img = Image.open(image_filename)
    img = img.convert('RGB')
    
    pixels = list(img.getdata())

    # Filter
    if color_filter_function is not None:
        pixels = [pixel for pixel in pixels if color_filter_function(pixel)]

    color_count = Counter(pixels)

    if color_filter_function is not None and not color_count:
        return None#, []
    
    dominant_color = color_count.most_common(1)[0][0] #[0][1] is the 'times'

    # Find similar colors (useful for making masks)
    #similar_colors = [color for color in color_count.keys() if is_similar(color, dominant_color, tolerance)]
    
    return dominant_color#, similar_colors

def get_most_common_rgb_color(image_filename):
    return _get_dominant_color(image_filename, PixelFilterFunction.is_green)


# def get_greenscreen_areas(image_filename):
#     from PIL import Image
#     import numpy as np

#     def dfs(image_array, visited, x, y, region):
#         # Verificar límites
#         if x < 0 or x >= image_array.shape[0] or y < 0 or y >= image_array.shape[1]:
#             return
#         # Verificar si el píxel ya fue visitado o no es verde
#         if visited[x, y] or not PixelFilterFunction.is_green(image_array[x, y]):
#             return

#         # Marcar el píxel como visitado
#         visited[x, y] = True
#         region.append((x, y))  # Añadir el píxel a la región

#         # Direcciones: verticales, horizontales y diagonales
#         directions = [
#             (1, 0),   # Abajo
#             (-1, 0),  # Arriba
#             (0, 1),   # Derecha
#             (0, -1),  # Izquierda
#             (1, 1),   # Abajo derecha
#             (1, -1),  # Abajo izquierda
#             (-1, 1),  # Arriba derecha
#             (-1, -1), # Arriba izquierda
#         ]

#         # Recursión para explorar vecinos en 8 direcciones
#         for dx, dy in directions:
#             dfs(image_array, visited, x + dx, y + dy, region)

#     def find_green_regions(image_path):
#         # Abrir la imagen
#         img = Image.open(image_path).convert('RGB')
#         image_array = np.array(img)
        
#         visited = np.zeros(image_array.shape[:2], dtype=bool)
#         regions = []

#         # Recorrer cada píxel
#         for x in range(image_array.shape[0]):
#             for y in range(image_array.shape[1]):
#                 if ColorFilterFunction.is_green(image_array[x, y]) and not visited[x, y]:
#                     region = []
#                     dfs(image_array, visited, x, y, region)  # Iniciar DFS
#                     if region:
#                         regions.append(region)

#         return regions
    
#     def filter_large_regions(regions):
#         filtered_regions = []
#         for region in regions:
#             if not any(all(p in r for p in region) for r in filtered_regions):
#                 filtered_regions.append(region)
#         return filtered_regions

#     green_regions = find_green_regions(image_filename)

#     print(f'Se encontraron {len(green_regions)} regiones verdes:')
#     for idx, region in enumerate(green_regions):
#         print(f'Región {idx + 1}: {region}')