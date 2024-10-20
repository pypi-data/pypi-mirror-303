from yta_multimedia.greenscreen.classes.greenscreen_details import GreenscreenDetails
from yta_multimedia.greenscreen.custom.utils import get_greenscreen_details
from yta_multimedia.greenscreen.enums import GreenscreenType
from yta_general_utils.checker.type import variable_is_type
from yta_general_utils.file.checker import file_is_video_file
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, vfx, concatenate_videoclips
from typing import Union

class VideoGreenscreen:
    greenscreen: GreenscreenDetails = None
    greenscreen_clip = None
    """
    The last greenscreen clip used to build a video. This clip will
    have the actual used greenscreen resource duration, so you can
    now how long is the greenscreen actually. You can use this clip
    to obtain the 'duration' when the 'from_image_to_video' or 
    'from_video_to_video' method is used so you can now how much 
    time is actually on greenscreen and how much is left because of
    the resource duration.

    You must remember that if a greenscreen of 3 seconds is applied
    over a video of 5 seconds of duration, only the 3 first secconds
    will be with the greenscreen, and the other 2 seconds will remain
    as in the original video.
    """

    def __init__(self, greenscreen: Union[GreenscreenDetails, str]):
        if variable_is_type(greenscreen, str):
            # We need to automatically detect greenscreen details
            greenscreen = get_greenscreen_details(greenscreen, GreenscreenType.VIDEO)

        self.greenscreen = greenscreen
       
    def from_image_to_image(self):
        # TODO: Does this make sense? We are working with a video, so
        # trying to generate just a frame, an image, does make sense?
        # TODO: By the way, this is not working yet
        pass

    def from_image_to_video(self, image_filename: str, duration: float = 3.0, output_filename: Union[str, None] = None):
        """
        Receives an 'image_filename', places it into the greenscreen and generates
        a video of 'duration' seconds of duration that is returned. This method
        will store locally the video if 'output_filename' is provided.
        """
        if not image_filename:
            return None
        
        if not duration:
            return None
        
        if not output_filename:
            return None
        
        imageclip = ImageClip(image_filename, duration = duration)
        final_clip = self.from_video_to_video(imageclip)

        if output_filename:
            final_clip.write_videofile(output_filename)

        return final_clip
    
    def from_video_to_image(self):
        # TODO: Does this make sense? By now it is not implemented
        pass

    def from_video_to_video(self, video: Union[str, VideoFileClip, CompositeVideoClip, ImageClip], output_filename: Union[str, None] = None):
        """
        Inserts the provided 'video' in the greenscreen and returns the
        CompositeVideoClip that has been created. If 'output_filename' 
        provided, it will be written locally with that file name.

        The provided 'video' can be a filename or a moviepy video clip.

        TODO: Careful when video is longer than greenscreen
        """
        if not video:
            return None
        
        if variable_is_type(video, str):
            if not file_is_video_file(video):
                return None
            
            video = VideoFileClip(video)

        # TODO: Change this 
        # We could have different areas in which append 1 or more 
        # videos, so it would be handled different. By now I'm
        # considering we only have one

        TMP_FILENAME = self.greenscreen.get_filename()

        # We choose the first greenscreen area to work with
        # TODO: Now we can handle more than one, so this could be
        # improved in a near future by being able to make a 
        # 'from_videos_to_video' and accept more than 1 video
        greenscreen_area = self.greenscreen.greenscreen_areas[0]
        
        # Create the clip
        self.green_screen_clip = VideoFileClip(TMP_FILENAME).fx(vfx.mask_color, color = greenscreen_area.rgb_color, thr = 100, s = 5)

        width = greenscreen_area.lower_right_pixel[0] - greenscreen_area.upper_left_pixel[0]
        # If the provided clip is shorter than our green screen: easy, crop the green screen
        # If the provided clip is longer than our green screen: I use the green screen duration
        # and let the clip be original the rest of the time
        # TODO: Improve resizing process as it is failing...
        if self.green_screen_clip.duration > video.duration:
            self.green_screen_clip = self.green_screen_clip.set_duration(video.duration)
            # Clip will be displayed inside the green screen area
            video = video.resize(width = width).set_position((greenscreen_area.upper_left_pixel[0], greenscreen_area.upper_left_pixel[1]))
            video = CompositeVideoClip([video, self.green_screen_clip], size = self.green_screen_clip.size)
        elif video.duration > self.green_screen_clip.duration:
            # First subclip will be displayed inside the green screen area
            first_clip = video.subclip(0, self.green_screen_clip.duration).resize(width = width).set_position((greenscreen_area.upper_left_pixel[0], greenscreen_area.upper_left_pixel[1]))
            # Second clip will be as the original one
            second_clip = video.subclip(self.green_screen_clip.duration, video.duration)
            video = concatenate_videoclips([
                CompositeVideoClip([first_clip, self.green_screen_clip], size = self.green_screen_clip.size),
                second_clip
            ])
        else:
            video = CompositeVideoClip([video, self.green_screen_clip], size = self.green_screen_clip.size)

        if output_filename:
            video.write_videofile(output_filename, fps = video.fps)

        return video