from yta_multimedia.greenscreen.classes.greenscreen_details import GreenscreenDetails
from yta_multimedia.greenscreen.custom.utils import get_greenscreen_details
from yta_multimedia.video.parser import VideoParser
from yta_multimedia.greenscreen.enums import GreenscreenType
from yta_general_utils.checker.type import variable_is_type
from yta_general_utils.image.parser import ImageParser
from moviepy.editor import ImageClip
from typing import Union
from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip, vfx, VideoClip
from PIL import Image, ImageDraw
from typing import Union, Any


class ImageGreenscreen:
    greenscreen: GreenscreenDetails = None

    def __init__(self, greenscreen: Union[GreenscreenDetails, str]):
        if variable_is_type(greenscreen, str):
            # We need to automatically detect greenscreen details
            greenscreen = get_greenscreen_details(greenscreen, GreenscreenType.IMAGE)

        self.greenscreen = greenscreen

    def __process_elements_and_save(self, output_filename):
        """
        Processes the greenscreen by writing the title, description
        and any other available element, and stores it locally as
        'output_filename' once processed.
        """
        base = Image.open(self.greenscreen.filename_or_google_drive_url)
        draw = ImageDraw.Draw(base)

        # TODO: I preserve this code for the future
        # # We need to write title if existing
        # if self.__title:
        #     title_position = (self.__title_x, self.__title_y)
        #     draw.text(title_position, self.__title, font = self.__title_font, fill = self.__title_color)

        # if self.__description:
        #     description_position = (self.__description_x, self.__description_y)
        #     draw.text(description_position, self.__description, font = self.__description_font, fill = self.__description_color)

        # TODO: Handle anything else here

        # We save the image
        base.save(output_filename, quality = 100)

    # TODO: Make this below expect a type 'Image', but 'Image' or
    # 'Image.Image' returns each arg must be a type. Got <module 
    # 'PIL.Image'
    def from_image_to_image(self, image: Union[str, Any], output_filename: Union[str, None] = None):
        """
        Receives an 'image', places it into the greenscreen and generates
        another image that is stored locally as 'output_filename'.
        """
        return self.from_images_to_image([image], output_filename)

    def from_images_to_image(self, images, output_filename: str = None):
        video = self.from_images_to_video(images, duration = 1 / 60)

        if output_filename:
            video.save_frame(output_filename, t = 0)

        return video.get_frame(t = 0)

    def from_image_to_video(self, image: str, duration: float, output_filename: Union[str, None] = None):
        """
        Receives an 'image', places it into the greenscreen and generates
        a video of 'duration' seconds of duration that is returned. This method
        will store locally the video if 'output_filename' is provided.
        """
        return self.from_images_to_video([image], duration, output_filename)

    def from_images_to_video(self, images, duration: float, output_filename: str = None):
        if len(images) > len(self.greenscreen.greenscreen_areas) or len(images) < len(self.greenscreen.greenscreen_areas):
            raise Exception(f'There are more or less images provided ({str(len(images))}) than available alphascreen regions ({str(len(self.greenscreen.greenscreen_areas))}).')

        for image in images:
            image = ImageParser.to_numpy(image)
        
        videos = []
        for image in images:
            videos.append(ImageClip(image, duration = duration).set_fps(60))

        return self.from_videos_to_video(videos, output_filename)
    
    def from_video_to_video(self, video: Union[str, VideoFileClip, CompositeVideoClip, ImageClip], output_filename: Union[str, None] = None):
        """
        Inserts the provided 'video' in the greenscreen and returns the
        CompositeVideoClip that has been created. If 'output_filename' 
        provided, it will be written locally with that file name.

        The provided 'video' can be a filename or a moviepy video clip.
        """
        return self.from_videos_to_video([video], output_filename)
    
    def from_videos_to_video(self, videos: list[Union[str, VideoClip]], output_filename: str = None):
        if len(videos) > len(self.greenscreen.greenscreen_areas):
            raise Exception(f'There are more videos provided ({str(len(videos))}) than available greenscreen regions ({str(len(self.greenscreen.greenscreen_areas))}).')

        for video in videos:
            video = VideoParser.to_moviepy(video)

        for index, video in enumerate(videos):
            videos[index] = self.greenscreen.greenscreen_areas[index].region.resize_video_to_fit_in(videos[index])

        TMP_FILENAME = self.greenscreen.get_filename()

        # I consider the same greenscreen rgb color for all areas
        green_screen_clip = ImageClip(TMP_FILENAME, duration = video.duration).fx(vfx.mask_color, color = self.greenscreen.greenscreen_areas[0].rgb_color, thr = 100, s = 5)

        final_clip = CompositeVideoClip([
            *videos, 
            green_screen_clip
        ], size = green_screen_clip.size)

        if output_filename:
            final_clip.write_videofile(output_filename)

        return final_clip