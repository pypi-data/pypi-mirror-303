from yta_multimedia.video.parser import VideoParser
from yta_general_utils.dimensions import adjust_to_aspect_ratio
from moviepy.editor import VideoClip
from moviepy.video.fx.all import crop
from typing import Union


def resize_video(video: Union[str, VideoClip], size, output_filename: Union[str, None] = None):
    """
    Resizes the video to the provided 'size' by cropping a
    region of the given 'video' that fits the 'size' aspect
    ratio and resizing that region to the 'size'.

    This method is using the whole video and then resizing,
    so the quality of the video is preserved and no small
    regions are used. The most part of the video is 
    preserved.

    This method returns the video modified.

    This method will write the video if 'output_filename' is
    provided.
    """
    video = VideoParser.to_moviepy(video)

    # We need to adjust the video to the AR of the given 'size'
    new_ar = size[0] / size[1]
    video_width, video_height = video.size
    new_video_size = adjust_to_aspect_ratio(video_width, video_height, new_ar)

    video = crop(video, width = new_video_size[0], height = new_video_size[1], x_center = video_width / 2, y_center = video_height / 2)

    # We resize it (up or down) to the desired 'size'
    video = video.resize((size[0], size[1]))

    if output_filename:
        video.write_videofile(output_filename)

    return video