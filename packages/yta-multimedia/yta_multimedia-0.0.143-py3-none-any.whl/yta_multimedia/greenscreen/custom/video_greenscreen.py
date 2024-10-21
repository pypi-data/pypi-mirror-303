from yta_multimedia.greenscreen.classes.greenscreen_details import GreenscreenDetails
from yta_multimedia.greenscreen.custom.utils import get_greenscreen_details
from yta_multimedia.video.edition.duration import set_video_duration, ExtendVideoMode
from yta_multimedia.video.parser import VideoParser
from yta_multimedia.greenscreen.enums import GreenscreenType
from yta_general_utils.image.parser import ImageParser
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
       
    def from_image_to_image(self, image, output_filename: str):
        # TODO: Does this make sense? We are working with a video, so
        # trying to generate just a frame, an image, does make sense?
        # TODO: By the way, this is not working yet
        return self.from_images_to_image(self, [image], output_filename)
    
    def from_images_to_image(self, images, output_filename: str):
        video = self.from_images_to_video(images, duration = 1 / 60)

        if output_filename:
            video.save_frame(output_filename, t = 0)

        return video.get_frame(t = 0)
    
    def from_image_to_video(self, image, duration: float, output_filename: str):
        return self.from_images_to_video([image], duration, output_filename)
    
    def from_images_to_video(self, images, duration: float, output_filename: str):
        if len(images) > len(self.greenscreen.greenscreen_areas) or len(images) < len(self.greenscreen.greenscreen_areas):
            raise Exception(f'There are more or less images provided ({str(len(images))}) than available alphascreen regions ({str(len(self.greenscreen.greenscreen_areas))}).')

        for image in images:
            image = ImageParser.to_numpy(image)
        
        videos = []
        for image in images:
            videos.append(ImageClip(image, duration = duration).set_fps(60))

        return self.from_videos_to_video(videos, output_filename)
    
    def from_video_to_video(self, video, output_filename: str):
        return self.from_videos_to_video([video], output_filename)
    
    def from_videos_to_video(self, videos, output_filename: str):
        if len(videos) > len(self.greenscreen.greenscreen_areas):
            raise Exception(f'There are more videos provided ({str(len(videos))}) than available greenscreen regions ({str(len(self.greenscreen.greenscreen_areas))}).')

        for video in videos:
            video = VideoParser.to_moviepy(video)

        for index, video in enumerate(videos):
            videos[index] = self.greenscreen.greenscreen_areas[index].region.resize_video_to_fit_in(videos[index])

        TMP_FILENAME = self.greenscreen.get_filename()

        # I consider the same greenscreen rgb color for all areas
        green_screen_clip = VideoFileClip(TMP_FILENAME).fx(vfx.mask_color, color = self.greenscreen.greenscreen_areas[0].rgb_color, thr = 100, s = 5)

        # Videos durations can be shorter than greenscreen
        for index, video in enumerate(videos):
            videos[index] = set_video_duration(videos[index], green_screen_clip.duration, ExtendVideoMode.FREEZE_LAST_FRAME)

        final_clip = CompositeVideoClip([
            *videos, 
            green_screen_clip
        ], size = green_screen_clip.size)

        if output_filename:
            final_clip.write_videofile(output_filename)

        return final_clip