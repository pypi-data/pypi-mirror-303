from yta_general_utils.checker.type import variable_is_type
from yta_general_utils.file.checker import file_is_audio_file, file_is_video_file
from yta_general_utils.file import rename_file
from yta_general_utils.temp import create_temp_filename
from moviepy.editor import VideoFileClip, AudioFileClip
from typing import Union

import ffmpeg


def extract_audio_from_video(video_input: Union[VideoFileClip, str], output_filename: Union[str, None] = None):
    """
    Returns the audio in the video file provided as 'video_input'. If
    'output_filename' provided, it will write the audio in a file
    with that name.
    """
    if not video_input:
        return None
    
    if variable_is_type(video_input, str):
        if not file_is_video_file(video_input):
            return None
            
        video_input = VideoFileClip(video_input)

    if output_filename:
        # TODO: Check extension, please
        video_input.write_audiofile(output_filename)

    return video_input.audio

def set_audio_in_video(video_input: Union[VideoFileClip, str], audio_input: Union[AudioFileClip, str], output_filename: Union[str, None] = None):
    """
    This method returns a VideoFileClip that is the provided 'video_input' 
    with the also provided 'audio_input' as the unique audio (if valid
    parameters are provided). If 'output_filename' provided, it will
    write the video file with the new audio with that provided name.

    (!) If the input video file and the output file name are the same, you 
    will lose the original as it will be replaced.
    """
    if not video_input:
        return None
    
    if variable_is_type(video_input, str):
        if not file_is_video_file(video_input):
            return None
        
        video_input = VideoFileClip(video_input)
    
    if not audio_input:
        return None
    
    if variable_is_type(audio_input, str):
        if not file_is_audio_file(audio_input):
            return None
        
        audio_input = AudioFileClip(audio_input)

    video_input = video_input.set_audio(audio_input)

    if output_filename:
        # TODO: Check extension, please
        tmp_output_filename = create_temp_filename('tmp_output.mp4')

        if variable_is_type(video_input, str) and variable_is_type(audio_input, str) and video_input and audio_input:
            # Both are valid str filenames, we will concat with ffmpeg
            # TODO: Check if I can get the original filename from an AudioFileClip|VideoFileClip
            ffmpeg.concat(ffmpeg.input(video_input), ffmpeg.input(audio_input), v = 1, a = 1).output(tmp_output_filename).run()
        else:
            video_input.write_videofile(tmp_output_filename)

        rename_file(tmp_output_filename, output_filename, True)

    return video_input

def set_audio_in_video_ffmpeg(video_filename: str, audio_filename: str, output_filename: str):
    """
    Sets the provided 'audio_filename' in the also provided 'video_filename'
    with the ffmpeg library and creates a new video 'output_filename' that
    is that video with the provided audio.

    TODO: This method need more checkings about extensions, durations, etc.
    """
    if not audio_filename:
        return None
    
    if not file_is_audio_file(audio_filename):
        return None
    
    if not video_filename:
        return None
    
    if not file_is_video_file(video_filename):
        return None
    
    if not output_filename:
        return None
    
    # TODO: What about longer audio than video (?)
    input_video = ffmpeg.input(video_filename)
    input_audio = ffmpeg.input(audio_filename)

    ffmpeg.concat(input_video, input_audio, v = 1, a = 1).output(output_filename).run(overwrite_output = True)