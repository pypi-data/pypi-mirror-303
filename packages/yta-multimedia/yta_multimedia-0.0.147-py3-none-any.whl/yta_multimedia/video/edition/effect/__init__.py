from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from yta_multimedia.video.parser import VideoParser
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip
from typing import Union


def apply_effect_to_video(video: Union[str, VideoFileClip, CompositeVideoClip, ImageClip], effect: VideoEffect, **kwargs):
    """
    This method will apply the provided 'effect' (if valid) to the also
    provided whole 'video' and will return the new clip with the effect
    applied.

    You can pass any effect customization parameter through the 'kwargs'
    parameters, but I recommend you to avoid this method and instantiate
    a valid 'effect', passing the 'video' to the initializer and using 
    the '.apply()' method like in this line below:
    > BlurMoviepyEffect(video).apply()

    The text above is easier for the developer because can check the 
    parameters accepted by the effect in the initializing process.
    """
    if not video:
        raise Exception('No "video" provided.')
    
    if not effect:
        raise Exception('No "effect" provided.')
    
    # We check if the parent of the effect is one of the 
    # expected ones
    # TODO: Maybe issubclass(effect, VideoEffect) (?)
    effect_parent_classes = effect.__bases__
    if VideoEffect in effect_parent_classes:
        raise Exception('Provided "effect" is not valid.')
    
    video = VideoParser.to_moviepy(video)
    
    # TODO: This is untested with the new effect version
    return effect.apply(video, **kwargs)

"""
# The effects that we are using here are the ones prepared for the
# segment, with information about the time and that stuff.

# Ok, this is a general method, not our main flow method.
# We just need to apply the effect in the video, so lets
# check that the effect is valid, apply on the video if
# possible, and return the video.
"""