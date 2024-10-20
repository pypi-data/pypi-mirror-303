
from yta_multimedia.video.utils import parse_parameter_as_moviepy_clip
from yta_multimedia.video.frames import get_frame_from_video_by_time
from yta_multimedia.video.generation import generate_video_from_image
from yta_general_utils.file.checker import file_is_video_file
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, ColorClip, concatenate_videoclips
from typing import Union
from enum import Enum


# TODO: Move this to a better place
class ExtendVideoMode(Enum):
    """
    This is a Enum to set the parameter option to extend the video
    duration with one of these modes (strategies).
    """
    LOOP = 'loop'
    """
    This mode will make the video loop (restart from the begining)
    until it reaches the expected duration.
    """
    FREEZE_LAST_FRAME = 'freeze_last_frame'
    """
    This mode will freeze the last frame of the video and extend 
    it until it reaches the expected duration.
    """


def set_video_duration(video: Union[str, VideoFileClip, CompositeVideoClip, ImageClip, ColorClip], duration = float, mode: ExtendVideoMode = ExtendVideoMode.LOOP):
    """
    This method will return a copy of the provided 'video' with the desired
    'duration' by applying crops or loops. If the provided 'duration' is
    lower than the actual 'video' duration, it will be shortened. If it is
    greater, it will be looped until we reach the desired 'duration'.

    The 'mode' provided will determine the way in which we extend the video
    duration if needed.

    This method makes a 'video.copy()' internally to work and avoid problems.
    """
    video = parse_parameter_as_moviepy_clip(video)

    if not duration:
        raise Exception('No "duration" provided.')
    
    if not mode:
        mode = ExtendVideoMode.LOOP

    if not isinstance(mode, ExtendVideoMode):
        raise Exception('Provided "mode" is not a ExtendVideoMode.')

    final_video = video.copy()

    if video.duration > duration:
        final_video = final_video.subclip(0, duration)
    elif video.duration < duration:
        if mode == ExtendVideoMode.LOOP:
            times_to_loop = (int) (duration / video.duration) - 1
            remaining_time = duration % video.duration
            for _ in range(times_to_loop):
                final_video = concatenate_videoclips([final_video, video])
            final_video = concatenate_videoclips([final_video, video.subclip(0, remaining_time)])
        elif mode == ExtendVideoMode.FREEZE_LAST_FRAME:
            remaining_time = duration - video.duration
            frame = get_frame_from_video_by_time(video, video.duration)
            frame_freezed_video = generate_video_from_image(frame, remaining_time)
            final_video = concatenate_videoclips([video, frame_freezed_video])

    return final_video