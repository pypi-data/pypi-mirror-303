from yta_multimedia.video.edition.effect.moviepy.position.objects.base_position_moviepy_effect import BasePositionMoviepyEffect
from yta_multimedia.video.edition.effect.moviepy.position.objects.coordinate_center import CoordinateCenter
from yta_multimedia.video.edition.effect.moviepy.position.objects.coordinate_corner import CoordinateCorner
from yta_multimedia.video.edition.effect.moviepy.position.enums import ScreenPosition
from yta_multimedia.video.edition.effect.moviepy.position.utils.position import get_moviepy_position
from yta_multimedia.video.edition.effect.moviepy.position.utils.move import arc_movement
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, ColorClip, VideoClip
from typing import Union


class MoveArcPositionMoviepyEffect(BasePositionMoviepyEffect):
    """
    Effect of moving the element from one place in the screen (or outside
    of bounds) to another, linearly.
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], initial_position: Union[ScreenPosition, CoordinateCorner, CoordinateCenter] = ScreenPosition.OUT_LEFT, final_position: Union[ScreenPosition, CoordinateCorner, CoordinateCenter] = ScreenPosition.CENTER, arc_is_bottom: bool = False, max_arc_height: float = 300):
        """
        Applies the effect to the 'video' provided when initializing this
        effect class, and puts the video over a static black background
        image of 1920x1080.
        """
        return cls.apply_over_video(BasePositionMoviepyEffect.get_black_background_clip(video.duration), initial_position, final_position, arc_is_bottom, max_arc_height)

    @classmethod
    def apply_over_video(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], background_video: Union[str, VideoClip, VideoFileClip, CompositeVideoClip, ImageClip, ColorClip], initial_position: Union[ScreenPosition, CoordinateCorner, CoordinateCenter] = ScreenPosition.OUT_LEFT, final_position: Union[ScreenPosition, CoordinateCorner, CoordinateCenter] = ScreenPosition.CENTER, arc_is_bottom: bool = False, max_arc_height: float = 300):
        """
        TODO: Write well

        Applies the effect on the video used when instantiating the
        effect, but applies the effect by placing it over the 
        'background_video' provided in this method (the 
        'background_video' will act as a background video for the 
        effect applied on the initial video).

        This method will set the video used when instantiating the
        effect as the most important, and its duration will be 
        considered as that. If the 'background_video' provided 
        has a duration lower than the original video, we will
        loop it to reach that duration. If the video is shorter
        than the 'background_video', we will crop the last one
        to fit the original video duration.
        """
        background_video = BasePositionMoviepyEffect.prepare_background_clip(background_video)

        BasePositionMoviepyEffect.validate_position(initial_position)
        BasePositionMoviepyEffect.validate_position(final_position)

        initial_position = get_moviepy_position(video, background_video, initial_position)
        final_position = get_moviepy_position(video, background_video, final_position)

        effect = video.set_position(lambda t: arc_movement(t, initial_position, final_position, video.duration, video.fps, arc_is_bottom, max_arc_height)).set_start(0).set_duration(video.duration)
        
        return CompositeVideoClip([
            background_video,
            effect
        ])