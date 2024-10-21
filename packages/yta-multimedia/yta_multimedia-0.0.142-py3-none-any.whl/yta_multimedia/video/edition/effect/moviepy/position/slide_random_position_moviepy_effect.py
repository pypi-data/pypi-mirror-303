from yta_multimedia.video.edition.effect.moviepy.position.objects.base_position_moviepy_effect import BasePositionMoviepyEffect
from yta_multimedia.video.edition.effect.moviepy.position.move import MoveLinearPositionMoviepyEffect
from yta_multimedia.video.edition.effect.moviepy.position.static import StayAtPositionMoviepyEffect
from yta_multimedia.video.edition.effect.moviepy.position.enums import ScreenPosition
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, concatenate_videoclips, ColorClip, VideoClip
from typing import Union


class SlideRandomPositionMoviepyEffect(BasePositionMoviepyEffect):
    """
    Effect of appearing from TOP, TOP_LEFT, BOTTOM, RIGHT, etc. 
    staying at the center, and dissapearing from the opposite 
    edge. This animation will spend 1/6 of the time in the 
    entrance, 4/6 of the time staying at the center, and 1/6 of 
    the time in the exit.
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip]):
        return cls.apply_over_video(video, BasePositionMoviepyEffect.get_black_background_clip(video.duration))

    @classmethod
    def apply_over_video(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], background_video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip]):
        background_video = BasePositionMoviepyEffect.prepare_background_clip(background_video, video)

        random_position = ScreenPosition.in_and_out_positions_as_list()

        movement_time = background_video.duration / 6
        stay_time = background_video.duration / 6 * 4

        effect = concatenate_videoclips([
            MoveLinearPositionMoviepyEffect(video.subclip(0, movement_time)).apply_over_video(background_video.subclip(0, movement_time), random_position[0], ScreenPosition.CENTER),
            StayAtPositionMoviepyEffect(video.subclip(movement_time, movement_time + stay_time)).apply_over_video(background_video.subclip(movement_time, movement_time + stay_time), ScreenPosition.CENTER),
            MoveLinearPositionMoviepyEffect(video.subclip(movement_time + stay_time, video.duration)).apply_over_video(background_video.subclip(movement_time + stay_time, video.duration), ScreenPosition.CENTER, random_position[1])
        ])

        return effect