from yta_multimedia.video.edition.effect.moviepy.position.objects.base_position_moviepy_effect import BasePositionMoviepyEffect
from yta_multimedia.video.edition.effect.moviepy.position.objects.coordinate_center import CoordinateCenter
from yta_multimedia.video.edition.effect.moviepy.position.objects.coordinate_corner import CoordinateCorner
from yta_multimedia.video.edition.effect.moviepy.position.enums import ScreenPosition
from yta_multimedia.video.edition.effect.moviepy.position.utils.position import get_moviepy_position
from yta_multimedia.video.edition.effect.moviepy.position.utils.move import circular_movement
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, VideoClip, ColorClip
from typing import Union


class CirclesAtPositionMoviepyEffect(BasePositionMoviepyEffect):
    """
    Effect of moving in circles surrounding the specified position.

    TODO: Implement the radius parameter option
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], position: Union[ScreenPosition, CoordinateCorner, CoordinateCenter] = ScreenPosition.RANDOM_INSIDE):
        return cls.apply_over_video(video, BasePositionMoviepyEffect.get_black_background_clip(video.duration), position)

    @classmethod
    def apply_over_video(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], background_video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], position: Union[ScreenPosition, CoordinateCorner, CoordinateCenter] = ScreenPosition.RANDOM_INSIDE):
        BasePositionMoviepyEffect.validate_position(position)

        background_video = BasePositionMoviepyEffect.prepare_background_clip(background_video, video)

        position = get_moviepy_position(video, background_video, position)

        effect = video.set_position(lambda t: circular_movement(t, position[0], position[1])).set_start(0).set_duration(video.duration)

        return CompositeVideoClip([
            background_video,
            effect
        ])