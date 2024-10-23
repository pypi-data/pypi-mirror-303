from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, clips_array, VideoClip, ColorClip
from typing import Union
from math import log as math_log, pow as math_pow


class MultipliedVideoEffect(VideoEffect):
    """
    Generates a clips array with the provided 'clip' being shown
    'times' times (this parameter must be a pow of 4). This
    method has been created to be used internally with our own
    default methods.
    """
    
    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], times: int = None):
        """
        Applies the effect to the provided 'video'.
        """
        video = VideoEffect.parse_moviepy_video(video)

        if not times:
            times = 4

        audio = video.audio
        size = (video.w, video.h)

        # We will dynamically build the matrix
        row = []
        group = []
        # 4^3 = 64 => 8x8 = 2^3x2^3  and  4^2 = 16 => 4x4 = 2^2x2^2
        range_limit_value = math_pow(2, math_log(times, 4))
        for i in range(int(times / range_limit_value)):
            row = []
            for j in range(int(times / range_limit_value)):
                row.append(video)
            group.append(row)

        # When building 'clips_array' you sum the resolutions, so if you add four videos
        # of 1920x1080, you'll get one video of 4x(1920x1080) that will be impossible to
        # exported and unexpected. We resize it to avoid this and we don't resize each
        # clip before because they lose quality
        return clips_array(group).resize(size).set_audio(audio)