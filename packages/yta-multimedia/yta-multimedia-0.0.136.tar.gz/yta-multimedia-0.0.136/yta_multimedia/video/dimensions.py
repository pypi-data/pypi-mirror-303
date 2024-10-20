from yta_general_utils.temp import create_temp_filename
from yta_general_utils.checker.type import variable_is_type
from yta_general_utils.file import rename_file
from yta_general_utils.file.checker import file_is_video_file
from moviepy.editor import VideoFileClip
from math import floor, ceil
from typing import Union


def rescale_video(video_input: Union[VideoFileClip, str], output_width: int = 1920, output_height: int = 1080, output_filename: Union[str, None] = None):
    """
    This method was created to rescale videos upper to 1920x1080 or 1080x1920. This is,
    when a 4k video appears, we simplify it to 1080p resolution to work with only that
    resolution. This method returns the VideoFileClip rescaled but also writes it if
    'output_filename' provided.

    The 'output_width' and 'output_height' variables must be [1920 and 1080] or [1080 and
    1920]. Any other pair is not valid.

    This method is used in the script-guided video generation. Please, do not touch =).

    TODO: This method is very strict, so it will need a revision to allow other dimensions
    and keep scaling.
    """
    # We only want to accept 16/9 or 9/16 by now, so:
    if not (output_width == 1920 and output_height == 1080) and not (output_width == 1080 and output_height == 1920):
        print('Sorry, not valid input parameters.')
        return None
    
    if not video_input:
        return None
    
    if variable_is_type(video_input, str):
        if not file_is_video_file(video_input):
            return None
        
        video_input = VideoFileClip(video_input)
    
    SCALE_WIDTH = 16
    SCALE_HEIGHT = 9
    if output_width == 1080 and output_height == 1920:
        SCALE_WIDTH = 9
        SCALE_HEIGHT = 16

    width = video_input.w
    height = video_input.h

    # We avoid things like 1927 instead of 1920
    new_width = width - width % SCALE_WIDTH
    new_height = height - height % SCALE_HEIGHT

    proportion = new_width / new_height

    if proportion > (SCALE_WIDTH / SCALE_HEIGHT):
        print('This video has more width than expected. Cropping horizontally.')
        while (new_width / new_height) != (SCALE_WIDTH / SCALE_HEIGHT):
            new_width -= SCALE_WIDTH
    elif proportion < (SCALE_WIDTH / SCALE_HEIGHT):
        print('This video has more height than expected. Cropping vertically.')
        while (new_width / new_height) != (SCALE_WIDTH / SCALE_HEIGHT):
            new_height -= SCALE_HEIGHT

    print('Final: W' + str(new_width) + ' H' + str(new_height))
    videoclip_rescaled = video_input.crop(x_center = floor(width / 2), y_center = floor(height / 2), width = new_width, height = new_height)
    
    # Force output dimensions
    if new_width != output_width:
        print('Forcing W' + str(output_width) + ' H' + str(output_height))
        videoclip_rescaled = videoclip_rescaled.resize(width = output_width, height = output_height)

    if output_filename:
        # TODO: Check extension
        tmp_video_filename = create_temp_filename('scaled.mp4')
        tmp_audio_filename = create_temp_filename('temp-audio.m4a')
        videoclip_rescaled.write_videofile(tmp_video_filename, codec = 'libx264', audio_codec = 'aac', temp_audiofile = tmp_audio_filename, remove_temp = True)
        rename_file(tmp_video_filename, output_filename, True)

    return videoclip_rescaled

def resize_video(video_input: Union[VideoFileClip, str], new_width: int = None, new_height: int = None, output_filename: Union[str, None] = None):
    """
    Resizes the provided 'video_input' to the also provided 'new_width' and
    'new_height' without scaling. You can provide only one dimension and it
    will calculate the other one keeping the scale.

    This method will return the new video as a VideoFileClip and will write
    a new file only if 'output_filename' is provided.
    """
    if not new_width and not new_height:
        return None
    
    if not video_input:
        return None
    
    if variable_is_type(video_input, str):
        if not file_is_video_file(video_input):
            return None
        
        video_input = VideoFileClip(video_input)

    if new_width and not new_height:
        new_height = ceil((video_input.h * new_width) / video_input.w)
    elif new_height and not new_width:
        new_width = ceil((video_input.w * new_height) / video_input.h)

    # moviepy resize method does not allow odd numbers
    new_width -= new_width % 2
    new_height -= new_height % 2
    
    video_input = video_input.resize(width = new_width, height = new_height)

    if output_filename:
        video_input.write_videofile(output_filename)

    return video_input