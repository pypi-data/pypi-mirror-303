from yta_general_utils.file.checker import file_is_video_file
from yta_general_utils.file.filename import filename_is_type, FileType
from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, ImageClip
from typing import Union


# TODO: Deprecated (?)
def video_to_moviepy_video(video: Union[str, VideoFileClip, CompositeVideoClip, ColorClip, ImageClip]):
    """
    This method is a helper to turn the provided 'video' to a moviepy
    video type. If it is any of the moviepy video types specified in
    method declaration, it will be returned like that. If not, it will
    be load as a VideoFileClip if possible, or will raise an Exception
    if not.
    """
    if not video:
        raise Exception('No "video" provided.')
    
    if not isinstance(video, str) and not isinstance(video, VideoFileClip) and not isinstance(video, CompositeVideoClip) and not isinstance(video, ColorClip) and not isinstance(video, ImageClip):
        raise Exception('The "video" parameter provided is not a valid type. Check valid types in method declaration.')
    
    if isinstance(video, str):
        if not filename_is_type(video, FileType.VIDEO):
            raise Exception('The "video" parameter provided is not a valid video filename.')
        
        if not file_is_video_file(video):
            raise Exception('The "video" parameter is not a valid video file.')
        
        video = VideoFileClip

    return video
