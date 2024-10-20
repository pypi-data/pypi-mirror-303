from yta_multimedia.video.generation.manim.constants import SCENE_HEIGHT, SCENE_WIDTH
from manim import *


def width_to_manim_width(width):
    """
    You provide a real width in pixels (maybe 1920) and it is returned in the
    manim equivalent width. We consider a 16:9 proportion and 1920 as the
    maximum valid width.

    This method is built by myself to work better with a 16:9 proportion of 
    1920x1080 pixels. The manim system is different, so I made this to
    simplify the process.
    """
    return (width * SCENE_WIDTH) / 1920

def manim_width_to_width(width):
    """
    TODO: Write help
    """
    return (width * 1920) / SCENE_WIDTH

def height_to_manim_height(height):
    """
    You provide a real height in pixels (maybe 1080) and it is returned in the
    manim equivalent pixels. We consider 16:9 proportion and 1080 as the 
    maximum valid height.

    This method is built by myself to work better with a 16:9 proportion of 
    1920x1080 pixels. The manim system is different, so I made this to
    simplify the process.
    """
    return (height * SCENE_HEIGHT) / 1080

def manim_height_to_height(height):
    """
    TODO: Write help
    """
    return (height * 1080) / SCENE_HEIGHT




def fitting_text(text, width_to_fit: float = 1920, fill_opacity: float = 1, stroke_width: float = 0, color: ParsableManimColor = None, font_size: float = DEFAULT_FONT_SIZE, line_spacing: float = -1, font: str = '', slant: str = NORMAL, weight: str = NORMAL, t2c: dict[str, str] = None, t2f: dict[str, str] = None, t2g: dict[str, tuple] = None, t2s: dict[str, str] = None, t2w: dict[str, str] = None, gradient: tuple = None, tab_width: int = 4, warn_missing_font: bool = True, height: float = None, width: float = None, should_center: bool = True, disable_ligatures: bool = False, **kwargs):
    """
    This method returns a Text mobject that fits the provided 'width_to_fit'
    or, if the height is greater than the scene height, returns one with the
    greates possible width.
    
    This method has been built to be sure that your text is completely shown
    between the screen margins.

    @param
        **width_to_fit**
        The widht you want to fit, in normal pixels (1920 is the maximum). 
        These pixels will be processed to manim dimensions.
    """
    width_to_fit = width_to_manim_width(width_to_fit)

    txt_width_fitted = Text(text, fill_opacity, stroke_width, color, font_size, line_spacing, font, slant, weight, t2c, t2f, t2g, t2s, t2w, gradient, tab_width, warn_missing_font, height, width, should_center, disable_ligatures, **kwargs).scale_to_fit_width(width_to_fit)
    # I use a margin of 100 pixels so avoid being just in the borders
    txt_height_fitted = Text(text, fill_opacity, stroke_width, color, font_size, line_spacing, font, slant, weight, t2c, t2f, t2g, t2s, t2w, gradient, tab_width, warn_missing_font, height, width, should_center, disable_ligatures, **kwargs).scale_to_fit_height(SCENE_HEIGHT - height_to_manim_height(100))

    # As it is a 16:9 proportion, the height is the measure that limits the most
    if txt_height_fitted.font_size < txt_width_fitted.font_size:
        return txt_height_fitted
    return txt_width_fitted

def fitting_image(filename, width_to_fit, image_mode: str = 'RGBA', **kwargs):
    """
    Returns an ImageMobject of the provided 'filename' image that fits the provided 'width_to_fit'
    or, if the height limit is surpassed, that fits the height limit.

    @param
        **width_to_fit**
        The widht you want to fit, in normal pixels (1920 is the scene 
        width). These pixels will be processed to manim dimensions.
    """
    width_to_fit = width_to_manim_width(width_to_fit)

    image_width_fitted = ImageMobject(filename, image_mode, **kwargs).scale_to_fit_width(width_to_fit)
    image_height_fitted = ImageMobject(filename, image_mode, **kwargs).scale_to_fit_height(width_to_fit)

    # As it is a 16:9 proportion, the height is the measure that limits the most
    if image_height_fitted.width < image_width_fitted.width:
        return image_height_fitted
    
    return image_width_fitted

def fullscreen_image(filename, image_mode: str = 'RGBA', **kwargs):
    """
    Returns an ImageMobject that fits whole screen dimensions (1920x1080). It
    will ignore the dimension that is out of bounds.
    """
    image_width_fitted = ImageMobject(filename, image_mode, **kwargs).scale_to_fit_width(width_to_manim_width(1920))

    # We want the image that occupies the whole screen
    if manim_height_to_height(image_width_fitted.height) >= 1080:
        return image_width_fitted
    
    image_height_fitted = ImageMobject(filename, image_mode, **kwargs).scale_to_fit_height(height_to_manim_height(1080))

    return image_height_fitted

def preprocess_image(image: ImageMobject):
    """
    This method processes images bigger than our 1920x1080 dimensions and returns it
    scaled down to fit those dimensions. You should use this method as the first one
    when working with ImageMobjects, and then scaling it down as much as you need.
    """
    if manim_width_to_width(image.width) > 1920:
        image.scale_to_fit_width(width_to_manim_width(1920))
    if manim_height_to_height(image.height) > 1080:
        image.scale_to_fit_height(height_to_manim_height(1080))

    return image