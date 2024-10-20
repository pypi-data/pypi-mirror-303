from yta_multimedia.video.generation.manim.constants import HALF_SCENE_HEIGHT, HALF_SCENE_WIDTH
from yta_multimedia.video.generation.manim.utils.dimensions import width_to_manim_width, height_to_manim_height
from random import random


def get_random_position(width: float, height: float):
    """
    Returns a random position inside the screen according to the provided element width and
    height to fit in. If you are trying to position a text inside screen limits, you must
    provide text width and height to let this method calculate that random position.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT + (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_upper_left_position(width: float, height: float):
    """
    Returns a random position in the upper left corner according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = -(width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_upper_right_position(width: float, height: float):
    """
    Returns a random position in the upper right corner according to the 
    provided element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_upper_center_position(width: float, height: float):
    """
    Returns a random position in the upper center according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH / 2 + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH / 2 - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_upper_position(width: float, height: float):
    """
    Returns a random position in the upper section according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_center_position(width: float, height: float):
    """
    Returns a random position in the center according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH / 2 + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH / 2 - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT / 2 + (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT / 2 - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_center_left_position(width: float, height: float):
    """
    Returns a random position in the center left according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = -(width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT / 2 + (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT / 2 - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_center_right_position(width: float, height: float):
    """
    Returns a random position in the center right according to the 
    provided element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT / 2 + (height / 2)
    Y_MAXIMUM = HALF_SCENE_HEIGHT / 2 - (height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_lower_left_position(width: float, height: float):
    """
    Returns a random position in the lower left corner according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = -(width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT + (height / 2)
    Y_MAXIMUM = -(height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_lower_right_position(width: float, height: float):
    """
    Returns a random position in the lower right corner according to the 
    provided element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT + (height / 2)
    Y_MAXIMUM = -(height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_lower_center_position(width: float, height: float):
    """
    Returns a random position in the lower center according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH / 2 + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH / 2 - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT + (height / 2)
    Y_MAXIMUM = -(height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

def get_random_lower_position(width: float, height: float):
    """
    Returns a random position in the upper section according to the provided
    element 'width' and 'height' to fit in.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X_MINIMUM = -HALF_SCENE_WIDTH + (width / 2)
    X_MAXIMUM = HALF_SCENE_WIDTH - (width / 2)
    random_x = X_MINIMUM + (random() * (X_MAXIMUM - X_MINIMUM))
    Y_MINIMUM = -HALF_SCENE_HEIGHT + (height / 2)
    Y_MAXIMUM = -(height / 2)
    random_y = Y_MINIMUM + (random() * (Y_MAXIMUM - Y_MINIMUM))

    return {
        'x': random_x,
        'y': random_y
    }

# Exact places
HEIGHT_DISTANCE_FROM_EDGES = height_to_manim_height(10)
WIDTH_DISTANCE_FROM_EDGES = width_to_manim_width(10)
def get_upper_left_position(width: float, height: float):
    """
    Returns the exact position of the upper left corner according to
    the provided element 'width' and 'height' to fit in and be placed
    just in the corner.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = -HALF_SCENE_WIDTH + WIDTH_DISTANCE_FROM_EDGES + (width / 2)
    Y = HALF_SCENE_HEIGHT - HEIGHT_DISTANCE_FROM_EDGES - (height / 2)

    return {
        'x': X,
        'y': Y
    }

def get_upper_right_position(width: float, height: float):
    """
    Returns the exact position of the upper right corner according to
    the provided element 'width' and 'height' to fit in and be placed
    just in the corner.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = HALF_SCENE_WIDTH - WIDTH_DISTANCE_FROM_EDGES - (width / 2)
    Y = HALF_SCENE_HEIGHT - HEIGHT_DISTANCE_FROM_EDGES - (height / 2)

    return {
        'x': X,
        'y': Y
    }

def get_upper_center_position(height: float):
    """
    Returns the exact position of the upper center position according 
    to the provided element 'width' and 'height' to fit in and be 
    placed just there.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = 0
    Y = HALF_SCENE_HEIGHT - HEIGHT_DISTANCE_FROM_EDGES - (height / 2)

    return {
        'x': X,
        'y': Y
    }

def get_left_position(width: float):
    """
    Returns the exact position of the left side according to
    the provided element 'width' and 'height' to fit in and be placed
    just in that place

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = -HALF_SCENE_WIDTH + WIDTH_DISTANCE_FROM_EDGES + (width / 2)
    Y = 0

    return {
        'x': X,
        'y': Y
    }

def get_center_position():
    """
    Returns the exact position of the center according to the 
    provided element 'width' and 'height' to fit in and be placed
    just in that place

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = 0
    Y = 0

    return {
        'x': X,
        'y': Y
    }

def get_right_position(width: float):
    """
    Returns the exact position of the right side according to
    the provided element 'width' and 'height' to fit in and be placed
    just in that place

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = HALF_SCENE_WIDTH - WIDTH_DISTANCE_FROM_EDGES - (width / 2)
    Y = 0

    return {
        'x': X,
        'y': Y
    }

def get_lower_left_position(width: float, height: float):
    """
    Returns the exact position of the lower left corner according to
    the provided element 'width' and 'height' to fit in and be placed
    just in the corner.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = -HALF_SCENE_WIDTH + WIDTH_DISTANCE_FROM_EDGES + (width / 2)
    Y = -HALF_SCENE_HEIGHT + HEIGHT_DISTANCE_FROM_EDGES + (height / 2)

    return {
        'x': X,
        'y': Y
    }

def get_lower_right_position(width: float, height: float):
    """
    Returns the exact position of the lower right corner according to
    the provided element 'width' and 'height' to fit in and be placed
    just in the corner.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = HALF_SCENE_WIDTH - WIDTH_DISTANCE_FROM_EDGES - (width / 2)
    Y = -HALF_SCENE_HEIGHT + HEIGHT_DISTANCE_FROM_EDGES + (height / 2)

    return {
        'x': X,
        'y': Y
    }

def get_lower_center_position(height: float):
    """
    Returns the exact position of the lower center position according 
    to the provided element 'width' and 'height' to fit in and be 
    placed just there.

    Provided 'width' and 'height' must be in manim width and height.

    This method returns an object containing 'x' and 'y' random fitting
    coordinates.
    """
    X = 0
    Y = -HALF_SCENE_HEIGHT + HEIGHT_DISTANCE_FROM_EDGES + (height / 2)

    return {
        'x': X,
        'y': Y
    }