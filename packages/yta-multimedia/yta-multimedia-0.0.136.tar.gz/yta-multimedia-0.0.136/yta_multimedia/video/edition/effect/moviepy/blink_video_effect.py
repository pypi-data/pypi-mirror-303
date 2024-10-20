from yta_multimedia.video.edition.effect.open_close.fade_in_video_effect import FadeInVideoEffect
from yta_multimedia.video.edition.effect.open_close.fade_out_video_effect import FadeOutVideoEffect
from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, concatenate_videoclips, VideoClip, ColorClip
from typing import Union


class BlinkVideoEffect(VideoEffect):
    """
    This method makes the provided video blink, that is a composition of
    a FadeOut and a FadeIn consecutively to build this effect. The duration
    will be the whole clip duration. The FadeIn will last the half of the
    clip duration and the FadeOut the other half.

    The 'color' parameter is the color you want for the blink effect as the
    background color. The default value is black ([0, 0, 0]).
    """

    @staticmethod
    def apply(clip: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], color = None):
        """
        Applies the effect to the provided 'clip'.
        """
        clip = VideoEffect.parse_moviepy_video(clip)

        if color is None:
            color = [0, 0, 0]

        half_duration = clip.duration / 2
        clip = concatenate_videoclips([
            FadeOutVideoEffect.apply(clip.subclip(0, half_duration), duration = half_duration, color = color),
            FadeInVideoEffect.apply(clip.subclip(half_duration, clip.duration), duration = half_duration, color = color)
        ])

        return clip