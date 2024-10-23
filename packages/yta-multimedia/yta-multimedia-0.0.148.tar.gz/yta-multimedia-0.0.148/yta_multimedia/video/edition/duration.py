
from yta_multimedia.video.parser import VideoParser
from yta_multimedia.video.frames import VideoFrameExtractor
from yta_multimedia.video.generation import generate_video_from_image
from yta_general_utils.programming.enum import YTAEnum as Enum
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, ColorClip, concatenate_videoclips
from typing import Union


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
    video = VideoParser.to_moviepy(video)

    if not duration:
        raise Exception('No "duration" provided.')
    
    if not mode:
        mode = ExtendVideoMode.LOOP

    mode = ExtendVideoMode.to_enum(mode)

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
            frame = VideoFrameExtractor.get_frame_by_time(video, video.duration)
            frame_freezed_video = generate_video_from_image(frame, remaining_time)
            final_video = concatenate_videoclips([video, frame_freezed_video])

    return final_video