from yta_general_utils.file import checker as file_checker
from yta_general_utils.file import enums as file_enums
from yta_general_utils.file.filename import filename_is_type
from moviepy.editor import VideoFileClip, CompositeVideoClip, ColorClip, ImageClip
from typing import Union


class VideoParser:
    """
    Class to simplify the way we parse video parameters.
    """
    @classmethod
    def to_moviepy(cls, video: Union[str, VideoFileClip, CompositeVideoClip, ColorClip, ImageClip], has_mask: bool = False):
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
            if not filename_is_type(video, file_enums.FileType.VIDEO):
                raise Exception('The "video" parameter provided is not a valid video filename.')
            
            if not file_checker.file_is_video_file(video):
                raise Exception('The "video" parameter is not a valid video file.')
            
            video = VideoFileClip(video, has_mask = has_mask)

        # TODO: Maybe '.add_mask()' (?)

        return video
