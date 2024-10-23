from yta_multimedia.greenscreen.classes.greenscreen_details import GreenscreenDetails
from yta_multimedia.greenscreen.custom.utils import get_greenscreen_details
from yta_multimedia.video.edition.duration import set_video_duration, ExtendVideoMode
from yta_multimedia.alphascreen.masked_clip_creator import MaskedClipCreator
from yta_multimedia.video.parser import VideoParser
from yta_multimedia.greenscreen.enums import GreenscreenType
from yta_general_utils.image.parser import ImageParser
from yta_general_utils.checker.type import variable_is_type
from moviepy.editor import ImageClip, CompositeVideoClip, vfx, VideoClip, VideoFileClip
from typing import Union


class VideoGreenscreen:
    """
    Class representing a Video with some greenscreen regions on it
    that can be used to place other resources (images or videos)
    fitting those regions while this greenscreen video is displayed.

    This class is working as if the greenscreen regions in the image
    were static, so if it moves this won't work properly as it is 
    not mapping the region for all the frames, just for the first 
    one.

    TODO: Improve this by autodetecting all the greenscreen regions
    for each frame and storing them somewhere.
    """
    greenscreen: GreenscreenDetails = None
    """
    This parameter keeps the information about the greenscreen 
    regions that the video has, including their corner coordinates,
    the width, the height and the green color to apply the mask.
    """

    def __init__(self, greenscreen: Union[GreenscreenDetails, str]):
        # TODO: Enhance this by detecting greenscreens for each frame
        if variable_is_type(greenscreen, str):
            # We need to automatically detect greenscreen details
            greenscreen = get_greenscreen_details(greenscreen, GreenscreenType.VIDEO)

        self.greenscreen = greenscreen

        # TODO: Do this here to be able to use it in the masked_clip_creator
        TMP_FILENAME = self.greenscreen.get_filename()
        # I consider the same greenscreen rgb color for all areas
        greenscreen_clip = VideoFileClip(TMP_FILENAME).fx(vfx.mask_color, color = self.greenscreen.greenscreen_areas[0].rgb_color, thr = 100, s = 5)

        regions = [gsa.region for gsa in self.greenscreen.greenscreen_areas]

        self.masked_clip_creator = MaskedClipCreator(regions, greenscreen_clip)
       
    def from_image_to_image(self, image, output_filename: str):
        """
        Receives an 'image', places it into the greenscreen and generates
        an image with the first clip that is stored locally as
        'output_filename' if provided.
        """
        return self.masked_clip_creator.from_image_to_image(image, output_filename)
    
        # TODO: This is not returning RGBA only RGB
        return self.from_images_to_image(self, [image], output_filename)
    
    def from_images_to_image(self, images, output_filename: str):
        return self.masked_clip_creator.from_images_to_image(images, output_filename)
    
        video = self.from_images_to_video(images, duration = 1 / 60)

        if output_filename:
            video.save_frame(output_filename, t = 0)

        # TODO: This is not returning RGBA only RGB
        return video.get_frame(t = 0)
    
    def from_image_to_video(self, image, duration: float, output_filename: str):
        """
        Receives an 'image', places it into the greenscreen and generates
        a video of 'duration' seconds of duration that is returned. This method
        will store locally the video if 'output_filename' is provided.
        """
        return self.masked_clip_creator.from_image_to_video(image, duration, output_filename)
    
        return self.from_images_to_video([image], duration, output_filename)
    
    def from_images_to_video(self, images, duration: float, output_filename: str = None):
        return self.masked_clip_creator.from_images_to_video(images, duration, output_filename)
    
        if len(images) > len(self.greenscreen.greenscreen_areas) or len(images) < len(self.greenscreen.greenscreen_areas):
            raise Exception(f'There are more or less images provided ({str(len(images))}) than available greenscreen regions ({str(len(self.greenscreen.greenscreen_areas))}).')

        for image in images:
            image = ImageParser.to_numpy(image)
        
        videos = []
        for image in images:
            videos.append(ImageClip(image, duration = duration).set_fps(60))

        return self.from_videos_to_video(videos, output_filename)
    
    def from_video_to_video(self, video: Union[str, VideoClip], output_filename: str = None):
        """
        Inserts the provided 'video' in the greenscreen and returns the
        CompositeVideoClip that has been created. If 'output_filename' 
        provided, it will be written locally with that file name.

        The provided 'video' can be a filename or a moviepy video clip.
        """
        return self.masked_clip_creator.from_video_to_video(video, output_filename)

        return self.from_videos_to_video([video], output_filename)
    
    def from_videos_to_video(self, videos: list[Union[str, VideoClip]], output_filename: str = None):
        """
        Puts the provided 'videos' inside the greenscreen region by
        applying a mask, cropping the videos if necessary and rescaling
        them, also positioning to fit the region and returns the 
        CompositeVideoClip created.

        Videos can be longer or shorter than greenscreen clip. By now
        we are making that all videos fit the greenscreen duration. 
        That is achieved by enlarging or shortening them if necessary.
        Thats why results could be not as expected.

        TODO: Please, build some different strategies to apply here.
        """
        return self.masked_clip_creator.from_videos_to_video(videos, output_filename)

        if len(videos) > len(self.greenscreen.greenscreen_areas):
            raise Exception(f'There are more videos provided ({str(len(videos))}) than available greenscreen regions ({str(len(self.greenscreen.greenscreen_areas))}).')

        for video in videos:
            video = VideoParser.to_moviepy(video)

        for index, video in enumerate(videos):
            greenscreen_area_region = self.greenscreen.greenscreen_areas[index].region
            videos[index] = greenscreen_area_region.place_video_inside(videos[index])

        TMP_FILENAME = self.greenscreen.get_filename()

        # I consider the same greenscreen rgb color for all areas
        green_screen_clip = VideoFileClip(TMP_FILENAME).fx(vfx.mask_color, color = self.greenscreen.greenscreen_areas[0].rgb_color, thr = 100, s = 5)

        # TODO: Provided videos can be shorther than the greenscreen
        # or the greenscreen can be shorter than the videos, so we
        # need an strategy to follow. By now I'm forcing all the 
        # videos to fit the greenscreen duration by shortening or
        # enlarging them.

        # Adjust all videos to greenscreen video duration
        for index, video in enumerate(videos):
            videos[index] = set_video_duration(videos[index], green_screen_clip.duration, ExtendVideoMode.FREEZE_LAST_FRAME)

        final_clip = CompositeVideoClip([
            *videos, 
            green_screen_clip
        ], size = green_screen_clip.size)

        if output_filename:
            final_clip.write_videofile(output_filename)

        return final_clip