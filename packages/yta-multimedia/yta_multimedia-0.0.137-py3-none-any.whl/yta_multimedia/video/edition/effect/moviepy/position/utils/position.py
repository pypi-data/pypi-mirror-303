from yta_multimedia.video.edition.effect.moviepy.position.objects.coordinate_center import CoordinateCenter
from yta_multimedia.video.edition.effect.moviepy.position.objects.coordinate_corner import CoordinateCorner
from yta_multimedia.video.edition.effect.moviepy.position.enums import ScreenPosition
from yta_general_utils.file.checker import file_is_video_file
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, ColorClip
from typing import Union


def position_video_in(video: Union[str, VideoFileClip, CompositeVideoClip, ImageClip, ColorClip], background_video: Union[str, VideoFileClip, CompositeVideoClip, ImageClip, ColorClip], position: Union[ScreenPosition, CoordinateCenter, CoordinateCorner]):
    """
    Returns the 'video' positioned (with '.set_position(...)') to stay in 
    the provided 'position' without movement. It won't set any other
    property more than the duration (you will need to manually add
    '.set_duration()' or '.set_start()' if needed).

    This method will return the video positioned as a single element, so 
    make to wrap it properly in an array if it is part of a complex
    animation. 
    """
    if not video:
        raise Exception('No "video" provided.')
    
    if isinstance(video, str):
        if not file_is_video_file:
            raise Exception('Provided "video" is not a valid video file.')
        
        video = VideoFileClip(video)

    if not background_video:
        raise Exception('No "background_video" provided.')

    if isinstance(background_video, str):
        if not file_is_video_file:
            raise Exception('Provided "background_video" is not a valid video file.')
        
        background_video = VideoFileClip(background_video)

    if not isinstance(position, ScreenPosition):
        if not isinstance(position, tuple) and len(position) != 2:
            raise Exception('Provided "position" is not a valid ScreenPosition enum or (x, y) tuple.')
        
    position = get_moviepy_position(video, background_video, position)

    return video.set_position(position)


"""
    Coords related functions below
"""
def get_moviepy_position(video, background_video, position: Union[ScreenPosition, CoordinateCenter, CoordinateCorner]):
    """
    In the process of overlaying and moving the provided 'video' over
    the also provided 'background_video', this method calculates the
    (x, y) tuple position that would be, hypothetically, adapted from
    a 1920x1080 black color background static image. The provided 
    'position' will be transformed into the (x, y) tuple according
    to our own definitions in which the video (that starts in upper left
    corner) needs to be placed to fit the desired 'position'.
    """
    # TODO: Add 'video' and 'background_video' checkings
    if not video:
        raise Exception('No "video" provided.')
    
    if not background_video:
        raise Exception('No "background_video" provided.')
    
    if not position:
        raise Exception('No "position" provided.')
    
    if not isinstance(position, ScreenPosition) and not isinstance(position, CoordinateCenter) and not isinstance(position, CoordinateCorner):
        raise Exception('Provided "position" is not ScreenPosition, CoordinateCenter or CoordinateCorner.')
    
    position_tuple = None

    if isinstance(position, ScreenPosition):
        position_tuple = position.get_moviepy_position(video, background_video)
    elif isinstance(position, CoordinateCenter):
        position_tuple = position.recalculate_for_video(video, background_video)
    elif isinstance(position, CoordinateCorner):
        position_tuple = position.recalculate_for_video(background_video)

    return position_tuple