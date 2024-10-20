from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from yta_multimedia.video.edition.effect.moviepy.position.objects.coordinate_center import CoordinateCenter
from yta_multimedia.video.edition.effect.moviepy.position.objects.coordinate_corner import CoordinateCorner
from yta_multimedia.video.edition.effect.moviepy.position.enums import ScreenPosition
from yta_multimedia.video.edition.duration import set_video_duration
from moviepy.editor import ColorClip, VideoFileClip, CompositeVideoClip, ImageClip, VideoClip
from typing import Union


class BasePositionMoviepyEffect(VideoEffect):
    """
    Class created to test position effects and building objects
    to simplify their use in our system.
    """

    @classmethod
    def validate_position(cls, position: Union[ScreenPosition, CoordinateCorner, CoordinateCenter]):
        """
        Validates that the provided 'position' is an ScreenPosition, a
        CoordinateCenter or a CoordinateCorner, or raises an Exception
        if not.
        """
        if not isinstance(position, ScreenPosition) and not isinstance(position, CoordinateCenter) and not isinstance(position, CoordinateCorner):
            raise Exception('Provided "position" is not a valid ScreenPosition, CoordinateCenter or CoordinateCorner.')

    @classmethod
    def get_black_background_clip(cls, duration: float):
        return ColorClip((1920, 1080), [0, 0, 0], duration = duration)
    
    @classmethod
    def prepare_background_clip(cls, background_video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip]):
        """
        Prepares the provided 'background_video' by setting its duration to the same
        as the also provided 'video'. By default, the strategy is looping the 
        'background_video' if the 'video' duration is longer, or cropping it if it is
        shorter. This method returns the background_clip modified according to the
        provided 'video'.

        This method will raise an Exception if the provided 'video' or the provided
        'background_video' are not valid videos.
        """
        VideoEffect.parse_moviepy_video(background_video)
        VideoEffect.parse_moviepy_video(video)

        background_video = set_video_duration(background_video, video.duration)

        return background_video

    @classmethod
    def apply(cls, video: Union[VideoFileClip, CompositeVideoClip, ImageClip]):
        """
        Applies the effect to the 'video' provided when initializing this
        effect class, and puts the video over a static black background
        image of 1920x1080.
        """
        pass

        #return BasePositionMoviepyEffect.apply_over_video(video, BasePositionMoviepyEffect.get_black_background_clip(video.duration))
    
    @classmethod
    def apply_over_video(cls, video: Union[VideoFileClip, CompositeVideoClip, ImageClip], background_clip: Union[VideoFileClip, CompositeVideoClip, ImageClip]):
        """
        This method parses the provided 'clip' and 'background_clip' to
        ensure they are valid moviepy clips and also sets the 
        'background_clip' duration to fit the provided 'clip' duration.
        """
        pass
        
        # VideoEffect.parse_moviepy_video(video)
        # VideoEffect.parse_moviepy_video(background_clip)

        # background_clip = set_video_duration(background_clip, video.duration)

        # return background_clip