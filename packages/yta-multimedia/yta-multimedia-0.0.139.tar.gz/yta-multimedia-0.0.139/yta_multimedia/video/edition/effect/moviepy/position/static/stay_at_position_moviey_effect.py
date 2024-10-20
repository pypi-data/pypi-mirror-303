from yta_multimedia.video.edition.effect.moviepy.position.objects.base_position_moviepy_effect import BasePositionMoviepyEffect
from yta_multimedia.video.edition.effect.moviepy.position.objects.coordinate_center import CoordinateCenter
from yta_multimedia.video.edition.effect.moviepy.position.objects.coordinate_corner import CoordinateCorner
from yta_multimedia.video.edition.effect.moviepy.position.enums import ScreenPosition
from yta_multimedia.video.edition.effect.moviepy.position.utils.position import position_video_in
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, ColorClip, VideoClip
from typing import Union


class StayAtPositionMoviepyEffect(BasePositionMoviepyEffect):
    """
    Effect of keeping the given 'video' inmobile in a specific
    position given (if given as parameter when applying) or randomly
    generated (inside the bounds according to the also provided
    'background_video' dimensions).
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], position: Union[ScreenPosition, CoordinateCorner, CoordinateCenter] = ScreenPosition.RANDOM_INSIDE):
        return cls.apply_over_video(video, BasePositionMoviepyEffect.get_black_background_clip(video.duration), position)

    @classmethod
    def apply_over_video(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], background_video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], position: Union[ScreenPosition, CoordinateCorner, CoordinateCenter] = ScreenPosition.RANDOM_INSIDE):
        BasePositionMoviepyEffect.validate_position(position)

        background_video = BasePositionMoviepyEffect.prepare_background_clip(background_video, video)

        effect = position_video_in(video, background_video, position).set_start(0).set_duration(video.duration)

        return CompositeVideoClip([
            background_video,
            effect
        ])