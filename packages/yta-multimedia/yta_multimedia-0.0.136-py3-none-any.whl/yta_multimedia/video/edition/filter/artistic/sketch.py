from yta_multimedia.video.frames import get_all_frames_from_video
from yta_multimedia.image.edition.filter.sketch import image_to_sketch, image_to_line_sketch
from yta_general_utils.image.converter import pil_image_to_numpy
from yta_general_utils.checker.type import variable_is_type
from yta_general_utils.file.checker import file_is_video_file
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, ImageSequenceClip
from typing import Union
from types import FunctionType


def video_to_sketch_video(video: Union[str, VideoFileClip, CompositeVideoClip, ImageClip], output_filename: Union[str, None]):
    # TODO: Document it
    return __video_to_frame_by_frame_filtered_video(video, image_to_sketch, output_filename)

def video_to_line_sketch_video(video: Union[str, VideoFileClip, CompositeVideoClip, ImageClip], output_filename: Union[str, None]):
    """
    This method is very very slow. I should try to optimize it or just
    use not, because it doesn't make sense as a video.
    """
    # TODO: Document it
    return __video_to_frame_by_frame_filtered_video(video, image_to_line_sketch, output_filename)

def __video_to_frame_by_frame_filtered_video(video: Union[str, VideoFileClip, CompositeVideoClip, ImageClip], filter_func: FunctionType, output_filename: Union[str, None] = None):
    """
    Internal function to be used by any of our video editing methods
    that actually use image filter frame by frame. They do the same
    by only changing the filter we apply.
    """
    # TODO: Check if 'filter_func' is a function

    if not video:
        raise Exception('No "video" provided.')
    
    if variable_is_type(video, str):
        if not file_is_video_file(video):
            return None
        
        video = VideoFileClip(video)

    original_frames = get_all_frames_from_video(video)
    sketched_frames = []
    for original_frame in original_frames:
        sketched_frames.append(pil_image_to_numpy(filter_func(original_frame)))

    sketched_video = ImageSequenceClip(sketched_frames, fps = video.fps).set_audio(video.audio)

    if output_filename:
        sketched_video.write_videofile(output_filename)

    return sketched_video

