from yta_general_utils.temp import create_temp_filename
from yta_general_utils.file.checker import file_is_video_file
from yta_general_utils.checker.type import variable_is_type
from moviepy.editor import VideoFileClip
from typing import Union


def crop_video_using_key_frame_second(video_input: Union[VideoFileClip, str], key_frame_second: float, duration: float, output_filename: Union[str, None] = None):
    if not video_input:
        return None
    
    if variable_is_type(video_input, str):
        if not file_is_video_file(video_input):
            return None
        
        video_input = VideoFileClip(video_input)

    if not key_frame_second or key_frame_second < 0 or key_frame_second > video_input.duration:
        # We use the middle of the video as the key frame
        key_frame_second = video_input.duration / 2
    if not duration:
        duration = video_input.duration
    if duration > video_input.duration or duration <= 0:
        duration = video_input.duration

    if duration < video_input.duration:
        start_second = 0
        end_second = video_input.duration
        # Only if we have to crop it already
        half_duration = duration / 2
        if key_frame_second - half_duration < 0:
            # Start in 0.0
            start_second = 0
            end_second = duration
        elif key_frame_second + half_duration > video_input.duration:
            # End in 'video_input.duration'
            start_second = video_input.duration - duration
            end_second = video_input.duration
        else:
            # Use 'key_frame_second' as center
            start_second = key_frame_second - half_duration
            end_second = key_frame_second + half_duration

        video_input = video_input.subclip(start_second, end_second)

    if output_filename:
        # TODO: Check extension
        tmp_audiofilename = create_temp_filename('temp-audio.m4a')
        # TODO: Do I really need all those parameters?
        video_input.to_videofile(
            output_filename,
            codec = "libx264",
            temp_audiofile = tmp_audiofilename,
            remove_temp = True,
            audio_codec = 'aac' # pcm_s16le or pcm_s32le
        )

    return video_input