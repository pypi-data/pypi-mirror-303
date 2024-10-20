"""
    @DEPRECATED

    This effect must be removed because of a new one with no Image
    manipulation.

    TO
"""

from yta_multimedia.video.edition.effect.moviepy.moviepy_effect import MoviepyEffect
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from typing import Union
from PIL import Image

import numpy as np
import math


class ZoomInMoviepyEffect(MoviepyEffect):
    """
    This effect will zoom in the clip, on the center.
    """
    __parameters = {}

    def __init__(self, clip: Union[VideoFileClip, CompositeVideoClip, ImageClip], zoom_ratio = None):
        self.__clip = clip

        if zoom_ratio is None:
            zoom_ratio = 0.01

        self.__parameters['zoom_ratio'] = zoom_ratio

    def process_parameters(self):
        if not self.__parameters['zoom_ratio']:
            self.__parameters['zoom_ratio'] = 0.01
        else:
            # Zoom is by now limited to [0.01 - 0.2] ratio
            if self.__parameters['zoom_ratio'] > 0.2:
                self.__parameters['zoom_ratio'] = 0.2
            elif self.__parameters['zoom_ratio'] <= 0.01:
                self.__parameters['zoom_ratio'] = 0.01

        return self.__parameters
    
    def __effect_calculations(self, get_frame, t, zoom_ratio):
        img = Image.fromarray(get_frame(t))
        base_size = img.size

        new_size = [
            math.ceil(img.size[0] * (1 + (zoom_ratio * t))),
            math.ceil(img.size[1] * (1 + (zoom_ratio * t)))
        ]

        # The new dimensions must be even.
        new_size[0] = new_size[0] + (new_size[0] % 2)
        new_size[1] = new_size[1] + (new_size[1] % 2)

        img = img.resize(new_size, Image.LANCZOS)

        x = math.ceil((new_size[0] - base_size[0]) / 2)
        y = math.ceil((new_size[1] - base_size[1]) / 2)

        img = img.crop([
            x, y, new_size[0] - x, new_size[1] - y
        ]).resize(base_size, Image.LANCZOS)

        result = np.array(img)
        img.close()

        return result
    
    def apply(self):
        """
        Applies the effect to the provided 'clip' and with the also
        provided parameters needed by this effect.
        """
        return self.__clip.fl(lambda get_frame, t: self.__effect_calculations(get_frame, t, **self.process_parameters()))
