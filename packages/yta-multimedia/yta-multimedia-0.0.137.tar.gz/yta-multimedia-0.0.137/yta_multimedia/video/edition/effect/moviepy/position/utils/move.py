import numpy as np
import math


"""
        In place movements (static) effect position functions below
"""
def circular_movement(t, x, y, radius: int = 200, cicle_time: float = 2):
    """
    Returns the (x, y) position tuple for the moviepy '.set_position()' effect,
    for each 't' provided, that will make the element move in circles with the
    provided 'radius'. The 'radius' parameter is the distance between the origin
    and the path the clip will follow. The 'cicle_time' is the time (in seconds)
    needed for a complete circle to be completed by the movement.

    If you provide the video duration as 'cicle_time', the video will make only
    one whole circle
    """
    # TODO: Do checkings
    return x + radius * np.cos((t / cicle_time) * 2 * math.pi), y + radius * np.sin((t / cicle_time) * 2 * math.pi)


"""
        With displacement (move) effect position functions below
"""
def linear_movement(t, initial_position: tuple, final_position: tuple, duration: float, fps: int):
    """
    Returns the (x, y) position tuple for the moviepy '.set_position()' method,
    for each 't' provided', that will make the element move doing a linear
    movement from the 'initial_position' to the 'final_position' in the given
    'duration' time.
    """
    # TODO: Do checkings
    progress = __get_current_movement_progress(t, duration, fps)
    x = initial_position[0] + progress * (final_position[0] - initial_position[0])
    y = initial_position[1] + progress * (final_position[1] - initial_position[1])

    return x, y

def sinusoidal_movement(t, initial_position: tuple, final_position: tuple, duration, fps: int):
    """
    Returns the (x, y) position tuple for the moviepy '.set_position()' method,
    for each 't' provided, that will make the element move doing a sinusoidal
    movement from the 'initial_position' to the 'final_position' in the provided
    'duration' time.
    """
    # TODO: Do checkings
    progress = __get_current_movement_progress(t, duration, fps)
    amplitude = 100  # amplitude of the sine wave
    frequency = 2  # frequency of the sine wave
    x = initial_position[0] + (final_position[0] - initial_position[0]) * progress
    y = initial_position[1] + (final_position[1] - initial_position[1]) * progress + amplitude * np.sin(2 * np.pi * frequency * progress)
    return (x, y)

def wave_movement(t, initial_position: tuple, final_position: tuple, duration, fps: int):
    """
    Returns the (x, y) position tuple for the moviepy '.set_position()'
    method, for each 't' provided, that will make the element go to the
    'initial_position' to the 'final_position' by doing two arcs (a 
    wave), one top and one bottom.
    """
    # TODO: Do checkings
    progress = __get_current_movement_progress(t, duration, fps)
    x = initial_position[0] + (final_position[0] - initial_position[0]) * progress
    y_start = initial_position[1]
    y_end = final_position[1]
    
    # Parameters for the sinusoidal arc
    amplitude = 200  # Maximum height of the arc
    frequency = 2 * np.pi / (final_position[0] - initial_position[0])  # Controls the frequency of the sine wave
    offset = (final_position[0] - initial_position[0]) / 2  # Center of the arc
    
    # Sinusoidal curve: y = amplitude * sin(frequency * (x - offset)) + average_y
    average_y = (y_start + y_end) / 2
    y = amplitude * np.sin(frequency * (x - initial_position[0] - offset)) + average_y
    
    return (x, y)

def arc_movement(t, initial_position: tuple, final_position: tuple, duration, fps: int, arc_is_bottom = False, max_height: int = 300):
    """
    Returns the (x, y) position tuple for the moviepy '.set_position()'
    method, for each 't' provided, that will make the element go to the
    'initial_position' to the 'final_position' by doing one single 
    arc movement. The movement will be an arc above, or bottom if the
    'arc_is_bottom' parameter is set as True. The 'max_height' parameter
    is to set the maximum height of the arc.
    """
    # TODO: Do checkings
    progress = __get_current_movement_progress(t, duration, fps)
    x = initial_position[0] + (final_position[0] - initial_position[0]) * progress
    
    # Calculate the midpoint and the maximum y value
    midpoint_x = (initial_position[0] + final_position[0]) / 2
    midpoint_y = (initial_position[1] + final_position[1]) / 2
    if arc_is_bottom:
        midpoint_y += max_height
    else:
        midpoint_y -= max_height

    # Calculate the arc movement:   y = a(x - h)^2 + k
    if arc_is_bottom:
        a = 4 * max_height / ((final_position[0] - initial_position[0])**2)
        y = -a * (x - midpoint_x)**2 + midpoint_y
    else:
        a = -4 * max_height / ((final_position[0] - initial_position[0])**2)
        y = -a * (x - midpoint_x)**2 + midpoint_y
    
    return (x, y)
    
def __get_current_movement_progress(t, duration: float, fps: int = 60):
    """
    Returns the current movement progress measured by the division
    't / (duration - 1 / fps)', that is the progress of the movement
    animation at the current moment 't'.
    """
    if not t and t != 0:
        raise Exception('No "t" provided.')
    
    if not duration:
        raise Exception('No "duration" provided.')
    
    if not fps:
        raise Exception('No "fps" provided.')

    return t / (duration - 1 / fps)