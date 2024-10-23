from yta_general_utils.checker.type import variable_is_type
from yta_general_utils.temp import create_temp_filename
from yta_general_utils.file.writer import write_file
from moviepy.editor import VideoFileClip, ImageClip
from yta_multimedia.video.parser import VideoParser
from typing import Union
from subprocess import run
import numpy as np


# TODO: Remove, refactor or improve tis method below
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

# TODO: Move this to another file (maybe 'concatenation.py') (?)
def concatenate_videos_ffmpeg(videos_abspaths, output_abspath: str):
    """
    This method concatenates the videos provided in 'videos_abspaths'
    and builds a new video, stored locally as 'output_abspath'.

    This method uses ffmpeg to concatenate the videos, so they must
    have the same resolution.
    """
    text = ''
    for video_abspath in videos_abspaths:
        text += f'file \'{video_abspath}\'\n'

    filename = create_temp_filename('append_videos.txt')
    write_file(text, filename)

    # TODO: Make a custom call from python not as command
    command = 'ffmpeg -y -f concat -safe 0 -i ' + filename + ' -c copy ' + output_abspath
    run(command)
    
    return VideoFileClip(output_abspath)

def is_video_transparent(video):
    """
    Checks if the first frame of the mask of the given 'video'
    has, at least, one transparent pixel.
    """
    # We need to detect the transparency from the mask
    video = VideoParser.to_moviepy(video, has_mask = True)

    # We need to find, by now, at least one transparent pixel
    # TODO: I would need to check all frames to be sure of this above
    return np.any(video.mask.get_frame(t = 0) == 1)

"""
ChatGPT told me this:

pip install ffmpeg-python

import ffmpeg

# Define tu archivo de entrada y salida
filename = 'tu_archivo.txt'  # Cambia esto al nombre de tu archivo de lista
output_abspath = 'salida.mp4'  # Cambia esto al nombre de tu archivo de salida

# Ejecuta el comando con ffmpeg-python
ffmpeg.input(filename, format='concat', safe='0').output(output_abspath, c='copy').run(overwrite_output=True)
"""