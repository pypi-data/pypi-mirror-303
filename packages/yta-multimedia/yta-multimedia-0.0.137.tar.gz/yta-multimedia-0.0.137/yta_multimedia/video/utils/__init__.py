from yta_general_utils.checker.type import variable_is_type
from yta_general_utils.file.checker import file_exists, file_is_video_file
from yta_general_utils.temp import create_temp_filename
from yta_general_utils.file.writer import write_file
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, ColorClip, VideoClip
from typing import Union
from subprocess import run


def generate_videoclip_from_image(image_filename: Union[ImageClip, str], duration: float = 1, output_filename: Union[str, None] = None):
    """
    Receives an image as 'image_filename' and creates an ImageClip of
    'duration' seconds. It will be also stored as a file if 
    'output_filename' is provided.

    # TODO: Should this method go into 'video.utils' instead of here (?)
    """
    if not image_filename:
        return None
    
    if duration <= 0:
        return None
    
    if not duration:
        return None
    
    if variable_is_type(output_filename, str):
        if not output_filename:
            return None
    
    if variable_is_type(image_filename, str):
        # ADV: By now we are limiting this to 60 fps
        image_filename = ImageClip(image_filename).set_fps(60).set_duration(duration)

    if output_filename:
        image_filename.write_videofile(output_filename)

    return image_filename

def parse_parameter_as_moviepy_clip(video: Union[VideoFileClip, CompositeVideoClip, ImageClip, ColorClip, VideoClip, str], has_mask: bool = False):
    """
    Checks if the provided 'video' is a valid moviepy video, of any 
    type, and it is returned. If it is a string, it is check if the
    filename string is a valid video file and its loaded. Anything
    unexpected will raise an Exception.

    This method returns a the video as a moviepy clip.
    """
    if not video:
        raise Exception('No "video" provided.')
    
    if not isinstance(video, (VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip, str)):
        raise Exception('The "video" parameter provided is not a VideoFileClip nor a VideoClip nor a CompositeVideoClip nor an ImageClip nor a ColorClip nor a string.')
    
    if isinstance(video, str):
        if not file_exists(video):
            raise Exception('The "video" parameter provided file does not exist.')
        
        if not file_is_video_file(video):
            raise Exception('The "video" parameter provided file is not a valid video file.')
        
        video = VideoFileClip(video, has_mask = has_mask)

    # TODO: Maybe '.add_mask()' (?)

    return video

def concatenate_videos_ffmpeg(videos_abspath, output_abspath: str):
    """
    This method concatenates the videos provided in 'videos_abspath'
    and builds a new video, stored locally as 'output_abspath'.

    This method uses ffmpeg to concatenate the videos, so they must
    have the same resolution.
    """
    text = ''
    for video_abspath in videos_abspath:
        text += f'file \'{video_abspath}\'\n'

    filename = create_temp_filename('append_videos.txt')
    write_file(text, filename)

    # TODO: Make a custom call from python not as command
    command = 'ffmpeg -y -f concat -safe 0 -i ' + filename + ' -c copy ' + output_abspath
    run(command)
    
    return VideoFileClip(output_abspath)