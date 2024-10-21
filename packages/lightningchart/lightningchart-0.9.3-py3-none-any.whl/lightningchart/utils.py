from __future__ import annotations
from enum import Enum
import math
import random

try:
    import numpy as np
except ImportError:
    np = None
try:
    import pandas as pd
except ImportError:
    pd = None


class Themes(Enum):
    White = 0
    Black = 1
    Light = 2
    Dark = 3
    CyberSpace = 4
    TurquoiseHexagon = 5


CSS_COLOR_NAMES = {
    'aliceblue': '#f0f8ff', 'antiquewhite': '#faebd7', 'aqua': '#00ffff', 'aquamarine': '#7fffd4', 'azure': '#f0ffff',
    'beige': '#f5f5dc', 'bisque': '#ffe4c4', 'black': '#000000', 'blanchedalmond': '#ffebcd', 'blue': '#0000ff',
    'blueviolet': '#8a2be2', 'brown': '#a52a2a', 'burlywood': '#deb887', 'cadetblue': '#5f9ea0',
    'chartreuse': '#7fff00', 'chocolate': '#d2691e', 'coral': '#ff7f50', 'cornflowerblue': '#6495ed',
    'cornsilk': '#fff8dc', 'crimson': '#dc143c', 'cyan': '#00ffff', 'darkblue': '#00008b', 'darkcyan': '#008b8b',
    'darkgoldenrod': '#b8860b', 'darkgray': '#a9a9a9', 'darkgreen': '#006400', 'darkgrey': '#a9a9a9',
    'darkkhaki': '#bdb76b', 'darkmagenta': '#8b008b', 'darkolivegreen': '#556b2f', 'darkorange': '#ff8c00',
    'darkorchid': '#9932cc', 'darkred': '#8b0000', 'darksalmon': '#e9967a', 'darkseagreen': '#8fbc8f',
    'darkslateblue': '#483d8b', 'darkslategray': '#2f4f4f', 'darkslategrey': '#2f4f4f', 'darkturquoise': '#00ced1',
    'darkviolet': '#9400d3', 'deeppink': '#ff1493', 'deepskyblue': '#00bfff', 'dimgray': '#696969',
    'dimgrey': '#696969', 'dodgerblue': '#1e90ff', 'firebrick': '#b22222', 'floralwhite': '#fffaf0',
    'forestgreen': '#228b22', 'fuchsia': '#ff00ff', 'gainsboro': '#dcdcdc', 'ghostwhite': '#f8f8ff', 'gold': '#ffd700',
    'goldenrod': '#daa520', 'gray': '#808080', 'green': '#008000', 'greenyellow': '#adff2f', 'grey': '#808080',
    'honeydew': '#f0fff0', 'hotpink': '#ff69b4', 'indianred': '#cd5c5c', 'indigo': '#4b0082', 'ivory': '#fffff0',
    'khaki': '#f0e68c', 'lavender': '#e6e6fa', 'lavenderblush': '#fff0f5', 'lawngreen': '#7cfc00',
    'lemonchiffon': '#fffacd', 'lightblue': '#add8e6', 'lightcoral': '#f08080', 'lightcyan': '#e0ffff',
    'lightgoldenrodyellow': '#fafad2', 'lightgray': '#d3d3d3', 'lightgreen': '#90ee90', 'lightgrey': '#d3d3d3',
    'lightpink': '#ffb6c1', 'lightsalmon': '#ffa07a', 'lightseagreen': '#20b2aa', 'lightskyblue': '#87cefa',
    'lightslategray': '#778899', 'lightslategrey': '#778899', 'lightsteelblue': '#b0c4de', 'lightyellow': '#ffffe0',
    'lime': '#00ff00', 'limegreen': '#32cd32', 'linen': '#faf0e6', 'magenta': '#ff00ff', 'maroon': '#800000',
    'mediumaquamarine': '#66cdaa', 'mediumblue': '#0000cd', 'mediumorchid': '#ba55d3', 'mediumpurple': '#9370db',
    'mediumseagreen': '#3cb371', 'mediumslateblue': '#7b68ee', 'mediumspringgreen': '#00fa9a',
    'mediumturquoise': '#48d1cc', 'mediumvioletred': '#c71585', 'midnightblue': '#191970', 'mintcream': '#f5fffa',
    'mistyrose': '#ffe4e1', 'moccasin': '#ffe4b5', 'navajowhite': '#ffdead', 'navy': '#000080', 'oldlace': '#fdf5e6',
    'olive': '#808000', 'olivedrab': '#6b8e23', 'orange': '#ffa500', 'orangered': '#ff4500', 'orchid': '#da70d6',
    'palegoldenrod': '#eee8aa', 'palegreen': '#98fb98', 'paleturquoise': '#afeeee', 'palevioletred': '#db7093',
    'papayawhip': '#ffefd5', 'peachpuff': '#ffdab9', 'peru': '#cd853f', 'pink': '#ffc0cb', 'plum': '#dda0dd',
    'powderblue': '#b0e0e6', 'purple': '#800080', 'red': '#ff0000', 'rosybrown': '#bc8f8f', 'royalblue': '#4169e1',
    'saddlebrown': '#8b4513', 'salmon': '#fa8072', 'sandybrown': '#f4a460', 'seagreen': '#2e8b57',
    'seashell': '#fff5ee', 'sienna': '#a0522d', 'silver': '#c0c0c0', 'skyblue': '#87ceeb', 'slateblue': '#6a5acd',
    'slategray': '#708090', 'slategrey': '#708090', 'snow': '#fffafa', 'springgreen': '#00ff7f', 'steelblue': '#4682b4',
    'tan': '#d2b48c', 'teal': '#008080', 'thistle': '#d8bfd8', 'tomato': '#ff6347', 'turquoise': '#40e0d0',
    'violet': '#ee82ee', 'wheat': '#f5deb3', 'white': '#ffffff', 'whitesmoke': '#f5f5f5', 'yellow': '#ffff00',
    'yellowgreen': '#9acd32',
}


def convert_to_list(data):
    try:
        if isinstance(data, (int, float)):
            return [data]
        if np is None or pd is None:
            if isinstance(data, (list, dict, tuple, set)):
                return list(data)
            else:
                return data.tolist()

        if isinstance(data, (np.ndarray, pd.Series, pd.Index, pd.DataFrame)):
            return data.tolist()
        else:
            return list(data)
    except TypeError:
        raise TypeError('Data type is not supported')


class Color:
    def __init__(self, *args):
        self.validate_input(args)
        self.rgb = self.parse_input(args)
        self.hex = self.convert_to_hex(self.rgb)

    def validate_input(self, args):
        if not (len(args) == 1 and isinstance(args[0], str)) and not (
                3 <= len(args) <= 4 and all(0 <= val <= 255 for val in args)):
            raise ValueError(
                "Invalid input. Pass either a hex color string, CSS color name, or 3-4 integers for RGB(A).")

    def parse_input(self, args):
        if len(args) == 1:  # Hex color string or CSS color name
            return self.parse_hex_or_css(args[0])
        else:  # RGB(A) values
            return tuple(args)

    def parse_hex_or_css(self, value):
        if isinstance(value, str):
            value = value.lower()
            if value.lower() in CSS_COLOR_NAMES:
                return self.parse_hex(CSS_COLOR_NAMES[value])
            else:
                return self.parse_hex(value)
        else:
            raise ValueError(
                "Invalid input. Pass either a hex color string, CSS color name, or 3-4 integers for RGB(A).")

    def parse_hex(self, hex_string):
        hex_string = hex_string.lstrip('#')
        if len(hex_string) == 6:
            r, g, b = map(lambda x: int(x, 16), (hex_string[0:2], hex_string[2:4], hex_string[4:6]))
            return r, g, b
        elif len(hex_string) == 8:
            r, g, b, a = map(lambda x: int(x, 16), (hex_string[0:2], hex_string[2:4], hex_string[4:6], hex_string[6:8]))
            return r, g, b, a
        else:
            raise ValueError("Invalid hex color string. It should be either 6 or 8 characters long.")

    def convert_to_hex(self, value):
        if len(value) == 3:
            return "#{:02X}{:02X}{:02X}".format(*value)
        elif len(value) == 4:
            return "#{:02X}{:02X}{:02X}{:02X}".format(*value)
        else:
            raise ValueError("Invalid RGB(A) values.")

    def get_hex(self):
        return self.hex

    def get_rgba(self):
        return self.rgb


def generate_random_array(
        amount: int = 10,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0
) -> list[float]:
    """Generate a list of random numbers.

    Args:
        amount (int): The length of the list.
        min_value (int | float): Minimum possible value of any given number.
        max_value (int | float): Maximum possible value of any given number.
    """
    if not isinstance(amount, int) or not isinstance(min_value, (int, float)) or not isinstance(max_value,
                                                                                                (int, float)):
        raise ValueError(
            "Invalid input. Make sure amount is an integer and min_value, max_value are either ints or floats.")

    if min_value >= max_value:
        raise ValueError("min_value should be less than max_value.")

    random_numbers = [round(random.uniform(min_value, max_value), 3) for _ in range(amount)]
    return random_numbers


def generate_progressive_array(
        amount: int = 10,
        start_index: int = 0,
        step: int = 1
) -> list[int]:
    """Generate a list of progressive integers.

    Args:
        amount (int): The number of elements in the array.
        start_index (int): The starting value for the progressive sequence.
        step (int): The step size between consecutive elements.
    """
    if not all(isinstance(i, int) for i in [amount, start_index, step]):
        raise ValueError("Invalid input. Make sure all inputs (amount, start_index, step) are integers.")

    progressive_array = [start_index + i * step for i in range(amount)]
    return progressive_array


def generate_Box3D_data(
        amount: int = 25,
        start_index: int = 0,
        min_height: int | float = 0.0,
        max_height: int | float = 10.0
):
    """Generate random data for Box3D chart.

    Args:
        amount (int): The length of the data.
        start_index (int): The first x value.
        min_height (int | float): Minimum possible height for any given box.
        max_height (int | float): Maximum possible height for any given box.

    Returns:
        List of Box3D entries.
    """
    data = []
    root = int(math.sqrt(amount))
    for x in range(start_index, root):
        for z in range(start_index, root):
            height = random.uniform(min_height, max_height)
            data.append({
                'xCenter': x,
                'yCenter': min_height + height / 2,
                'zCenter': z,
                'xSize': 1,
                'ySize': height,
                'zSize': 1
            })
    return data


def generate_random_xy_data(
        amount: int = 1,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0
) -> list[dict[str, int | float]]:
    """Generate a list of random {x, y} objects.

    Args:
        amount (int): The number of {x, y} objects to generate.
        min_value (int | float): The minimum value for both x and y.
        max_value (int | float): The maximum value for both x and y.

    Returns:
        List of dictionaries containing x and y values.
    """
    if not isinstance(amount, int) or not isinstance(min_value, (int, float)) or not isinstance(max_value,
                                                                                                (int, float)):
        raise ValueError(
            "Invalid input. Make sure amount is an integer and min_value, max_value are either ints or floats.")

    if min_value >= max_value:
        raise ValueError("min_value should be less than max_value.")

    random_xy_data = [{
        'x': round(random.uniform(min_value, max_value), 3),
        'y': round(random.uniform(min_value, max_value), 3)
    } for _ in range(amount)]
    return random_xy_data


def generate_random_xyz_data(
        amount: int = 1,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0
) -> list[dict[str, int | float]]:
    """ Generate a list of random {x, y, z} objects.

        Args:
            amount (int): The number of {x, y, z} objects to generate.
            min_value (int | float): The minimum value for x, y, and z.
            max_value (int | float): The maximum value for x, y, and z.

        Returns:
            List of dictionaries containing x, y, and z values.
    """
    if not isinstance(amount, int) or not isinstance(min_value, (int, float)) or not isinstance(max_value,
                                                                                                (int, float)):
        raise ValueError(
            "Invalid input. Make sure amount is an integer and min_value, max_value are either ints or floats.")

    if min_value >= max_value:
        raise ValueError("min_value should be less than max_value.")

    random_xyz_data = [{'x': round(random.uniform(min_value, max_value), 3),
                        'y': round(random.uniform(min_value, max_value), 3),
                        'z': round(random.uniform(min_value, max_value), 3)} for _ in range(amount)]
    return random_xyz_data


def generate_progressive_xy_data(
        amount: int = 100,
        starting_from: int = 0,
        step: int = 1,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0,
        progressive_dimension: str = 'x'
) -> list[dict[str, int | float]]:
    """Generate n amount of XY datapoints that are progressive with respect to one dimension.

    Args:
        amount (int): The size of the generated dataset.
        starting_from (int): The starting point of the progressive axis.
        step: The step size between progressive elements.
        min_value (int | float): Minimum value of any given datapoint.
        max_value (int | float): Maximum value of any given datapoint.
        progressive_dimension (str): "x" or "y"

    Returns:
        List of dictionaries containing x and y values.
    """
    if not all(isinstance(i, (int, float)) for i in [amount, starting_from, step, min_value, max_value]):
        raise ValueError("Invalid input. Make sure all numeric inputs are either ints or floats.")

    if not isinstance(progressive_dimension, str) or progressive_dimension.lower() not in ['x', 'y']:
        raise ValueError("Invalid progressive_dimension. It should be either 'x' or 'y'.")

    if amount <= 0:
        raise ValueError("Amount should be a positive integer.")

    progressive_xy_data = []

    for i in range(amount):
        x = starting_from + i * step if progressive_dimension.lower() == 'x' else round(
            random.uniform(min_value, max_value), 3)
        y = starting_from + i * step if progressive_dimension.lower() == 'y' else round(
            random.uniform(min_value, max_value), 3)

        progressive_xy_data.append({'x': x, 'y': y})

    return progressive_xy_data


def generate_progressive_xyz_data(
        amount: int = 100,
        starting_from: int = 0,
        step: int = 1,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0,
        progressive_dimension: str = 'x'
) -> list[dict[str, int | float]]:
    """Generate n amount of XYZ datapoints that are progressive with respect to one axis.

    Args:
        amount (int): The size of the generated dataset.
        starting_from (int): The starting point of the progressive axis.
        step: The step size between progressive elements.
        min_value (int | float): Minimum value of any given datapoint.
        max_value (int | float): Maximum value of any given datapoint.
        progressive_dimension (str): "x", "y", or "z"

    Returns:
        List of dictionaries containing x, y, and z values.
    """
    if not all(isinstance(i, (int, float)) for i in [amount, starting_from, step, min_value, max_value]):
        raise ValueError("Invalid input. Make sure all numeric inputs are either ints or floats.")

    if not isinstance(progressive_dimension, str) or progressive_dimension.lower() not in ['x', 'y', 'z']:
        raise ValueError("Invalid progressive_dimension. It should be either 'x', 'y', or 'z'.")

    if amount <= 0:
        raise ValueError("Amount should be a positive integer.")

    progressive_xyz_data = []

    for i in range(amount):
        x = starting_from + i * step if progressive_dimension.lower() == 'x' else round(
            random.uniform(min_value, max_value), 3)
        y = starting_from + i * step if progressive_dimension.lower() == 'y' else round(
            random.uniform(min_value, max_value), 3)
        z = starting_from + i * step if progressive_dimension.lower() == 'z' else round(
            random.uniform(min_value, max_value), 3)

        progressive_xyz_data.append({'x': x, 'y': y, 'z': z})

    return progressive_xyz_data


def generate_random_matrix_data(
        columns: int,
        rows: int,
        min_value: int | float = 0.0,
        max_value: int | float = 1.0
) -> list[list[int | float]]:
    """Generate a (2D) matrix dataset with random values between a specific range.

    Args:
        columns (int): The amount of columns in the matrix.
        rows (int): The amount of rows in the matrix.
        min_value (int | float): Minimum value of any given point in the matrix.
        max_value (int | float): Maximum value of any given point in the matrix.

    Returns:
        List of lists containing values.
    """
    if not all(isinstance(i, (int, float)) for i in [columns, rows, min_value, max_value]):
        raise ValueError("Invalid input. Make sure all numeric inputs are either ints or floats.")

    if columns <= 0 or rows <= 0:
        raise ValueError("Columns and rows should be positive integers.")

    random_matrix_data = [[round(random.uniform(min_value, max_value), 3) for _ in range(columns)] for _ in range(rows)]
    return random_matrix_data
