from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, VideoClip, ColorClip
from typing import Union


class ChangeSpeedVideoEffect(VideoEffect):
    """
    This effect changes the speed of the video to fit the requested
    'final_duration', that will accelerate or decelerate the video
    speed.
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], final_duration = None):
        """
        Applies the effect to the provided 'video'.
        """
        video = VideoEffect.parse_moviepy_video(video)

        if final_duration is None:
            final_duration = video.duration

        effect_name = VideoEffect.get_moviepy_vfx_effect('speedx')
        parameters = {
            'final_duration': final_duration
        }

        return video.fx(effect_name, **parameters)
