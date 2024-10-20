from yta_general_utils.checker.type import variable_is_type
from yta_general_utils.image.converter import numpy_image_to_pil
from moviepy.editor import ImageClip
from PIL import Image
from typing import Union, Any

import numpy as np


# TODO: I don't know if I should put this in another file or not...
# effect: segments.building.objects.effect.Effect = None
def generate_video_from_image(image: Union[str, Any], duration = 1, effect = None):
    """
    Genearates a ImageClip with the provided 'image_filename' that lasts the also
    provided 'duration'.

    This method will internally apply the 'effect' if provided. Check code or 
    developer guide to see available effects.
    """
    if not image:
        raise Exception('No "image" provided.')

    # if variable_is_type(image, str):
    #     # TODO: Check if image is actually an image
    #     # TODO: This image throws 'AttributeError: shape' moviepy error
    #     image = Image.open(image)
    # elif variable_is_type(image, np.ndarray):
    #     image = numpy_image_to_pil(image)

    if not variable_is_type(image, str):
        # TODO: Do something
        pass

    slide = ImageClip(image, duration = duration)
    slide = slide.set_fps(60)

    # TODO: This need work
    #slide = apply_effect(slide, effect)

    return slide