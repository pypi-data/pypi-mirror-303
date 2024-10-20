# TODO: Delete this when the title and description writing
# has been implemented in greenscreen new system.
from yta_multimedia.green_screen.custom_green_screen_image import CustomGreenScreenImage
from yta_general_utils.image.processor import get_green_screen_position
from yta_multimedia.resources.image.greenscreen.drive_urls import YOUTUBE_VIDEO_GREEN_SCREEN_GOOGLE_DRIVE_DOWNLOAD_URL
from yta_general_utils.downloader.google_drive import download_file_from_google_drive
from yta_general_utils.temp import create_temp_filename
from PIL import ImageFont
from os import getenv as os_getenv

# TODO: This was created to work with CustomGreenSreenImage, but I don't
# know where it is right now... I think it could be the new 
# TitledGreenScreenImage
class YoutubeVideoGreenScreen:
    # TODO: Move to .env (?)
    __FONTS_PATH = 'C:/USERS/DANIA/APPDATA/LOCAL/MICROSOFT/WINDOWS/FONTS/'

    def __init__(self, title):
        filename = download_file_from_google_drive(YOUTUBE_VIDEO_GREEN_SCREEN_GOOGLE_DRIVE_DOWNLOAD_URL, create_temp_filename('tmp.jpg'))
        # Detect color and edges automatically
        green_screen_info = get_green_screen_position(filename)
        rgb_color = green_screen_info['rgb_color']
        self.ulx = green_screen_info['ulx']
        self.uly = green_screen_info['uly']
        self.drx = green_screen_info['drx']
        self.dry = green_screen_info['dry']

        gs_width = self.drx - self.ulx
        gs_height = self.dry - self.uly
        aspect_ratio = gs_width / gs_height
        if aspect_ratio > (1920 / 1080):
            # We keep the width, but we calculate the height to keep 16/9 aspect ratio
            gs_height_for_16_9 = gs_width * (1080 / 1920)
            # Now we know the new height, so we only have to center the video on 'y' axis
            difference = gs_height_for_16_9 - gs_height
            # My video (16/9) will not fit the whole width
            self.uly -= difference / 2
            self.dry += difference / 2
        elif aspect_ratio < (1920 / 1080):
            # We keep the height, but we calculate the width to keep 16/9 aspect ratio
            gs_width_for_16_9 = gs_height * (1920 / 1080)
            # Now we know the new width, so we only have to center the video on 'x' axis
            difference = gs_width_for_16_9 - gs_width
            self.ulx -= difference / 2
            self.drx += difference / 2
        # TODO: Are we sure that those coords are int and make a real 16/9 with int numbers?

        title_font = ImageFont.truetype(self.__FONTS_PATH + 'ROBOTO-MEDIUM.TTF', 28, encoding = "unic")
        title_color = (0, 0, 0)
        title_x = 32
        title_y = 836

        self.cgsi = CustomGreenScreenImage(filename, rgb_color, self.ulx, self.uly, self.drx, self.dry, title, title_font, title_color, title_x, title_y, None, None, None, None, None)

    def save(self, output_filename):
        self.cgsi.save(output_filename)

    def insert_video(self, video_filename, output_filename):
        self.cgsi.insert_video(video_filename, output_filename)

    def from_clip(self, clip):
        """
        Receives a 'clip' and generates a new one that is the provided one inside of the
        green screen.
        """
        return self.cgsi.from_clip(clip)

    def insert_image(self, image_filename, output_filename):
        self.cgsi.insert_image(image_filename, output_filename)