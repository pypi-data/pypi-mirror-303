def zoom_in_t_func(zoom_ratio: float = 0.2):
    """
    Function that returns the resize value to make a moviepy
    video be zoomed in the 'zoom_ratio' zoom all the time.
    """
    return 1 + zoom_ratio

def zoom_out_t_func(zoom_ratio: float = 0.2):
    """
    Function that returns the resize value to make a moviepy
    video be zoomed out the 'zoom_ratio' zoom all the time.
    """
    return 1 - zoom_ratio

def linear_zoom_in_t_func(t, duration, zoom_ratio: float = 0.2):
    """
    Function that returns the resize value to make a moviepy
    video zoom in linearly to the 'zoom_ratio' zoom.
    """
    # TODO: Check 'zoom_ratio' is valid

    return 1 + zoom_ratio * (t / duration)

def linear_zoom_out_t_func(t, duration, zoom_ratio: float = 0.2):
    """
    Function that returns the resize value to make a moviepy
    video zoom out linearly to the 'zoom_ratio' zoom.
    """
    # TODO: Check 'zoom_ratio' is valid

    return 1 + zoom_ratio * (duration - (t / duration))

def linear_zoom_transition_t_func(t, duration, zoom_start: float = 1, zoom_end: float = 0.8):
    """
    Function that returns the resize value to make a moviepy
    video zoom in or out from the 'zoom_start' to the 'zoom_end'
    in the provided 'duration' time. If 'zoom_start' is greater
    than 'zoom_end' that will be a zoom out.
    """
    return zoom_start + (zoom_end - zoom_start) * (t / duration)

def logaritmic_zoom_transition_t_func(t, duration, zoom_start: float = 1, zoom_end: float = 0.8):
    # TODO: This has not been tested...
    import math

    zoom_start = math.log(zoom_start)
    zoom_end = math.log(zoom_end)

    # Interpolación logarítmica
    return math.exp(zoom_start + (zoom_end - zoom_start) * (t / duration))

