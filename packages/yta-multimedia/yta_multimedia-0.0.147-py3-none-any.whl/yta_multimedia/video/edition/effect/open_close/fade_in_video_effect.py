from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, ColorClip, VideoClip
from typing import Union


class FadeInVideoEffect(VideoEffect):
    """
    This effect will make the video appear progressively
    lasting the provided 'duration' time or the whole 
    clip time duration if None 'duration' provided.

    The 'color' provided must be an array containing
    the rgb colors (default is [0, 0, 0], which is black).
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], duration = None, color = None):
        """
        Applies the effect to the provided 'video'.
        """
        video = VideoEffect.parse_moviepy_video(video)

        if duration is None:
            duration = video.duration

        if color is None:
            color = [0, 0, 0]

        effect_name = VideoEffect.get_moviepy_vfx_effect('fadein')
        parameters = {
            'duration': duration,
            'initial_color': color
        }

        return video.fx(effect_name, **parameters)

