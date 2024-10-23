from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, ColorClip, VideoClip
from typing import Union


class BlackAndWhiteVideoEffect(VideoEffect):
    """
    This effect will make the clip appear in black and
    white colors.
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip]):
        """
        Applies the effect to the provided 'video'.
        """
        video = VideoEffect.parse_moviepy_video(video)

        effect_name = VideoEffect.get_moviepy_vfx_effect('blackwhite')
        parameters = {}

        return video.fx(effect_name, **parameters)
