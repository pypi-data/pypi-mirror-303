from yta_multimedia.video.parser import VideoParser
from moviepy.editor import vfx
from abc import ABC, abstractmethod


class VideoEffect(ABC):
    """
    Abstract class to be inherited by all my custom effects so I can 
    control they belong to this family.

    A video effect is an effect that is customly made by using 
    personal modifications, calculations, involving maybe some
    image manipulation, etc.

    A moviepy effect (or what I call like that) is an effect that is
    applied directly to the video by using only the moviepy editor
    and/or moviepy vfx module. It could be a simple moviepy effect
    made an object to simplify the work with it, or a more complex
    effect that is build with some different small effects.
    """

    @classmethod
    def parse_moviepy_video(cls, video, has_mask: bool = False):
        """
        Parses the provided video as a moviepy video clip returning it
        if valid or raising an Exception if invalid.
        """
        return VideoParser.to_moviepy(video, has_mask)
    
    @classmethod
    def get_moviepy_vfx_effect(cls, moviepy_effect_name: str):
        """
        Returns the moviepy vfx effect name corresponding to the provided
        'moviepy_effect_name'.
        """
        return getattr(vfx, moviepy_effect_name, None)

    @abstractmethod
    def apply(self):
        pass