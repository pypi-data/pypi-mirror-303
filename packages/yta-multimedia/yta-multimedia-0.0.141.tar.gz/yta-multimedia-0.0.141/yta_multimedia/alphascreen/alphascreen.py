from yta_multimedia.video.parser import VideoParser
from yta_multimedia.video.edition.resize import resize_video
from yta_general_utils.image.checker import has_transparency
from yta_general_utils.file.checker import is_valid_image
from yta_general_utils.dimensions import resize_to_fit_on_region
from yta_general_utils.image.region import ImageRegionFinder
from moviepy.editor import ImageClip, CompositeVideoClip
from PIL import Image

import numpy as np


class Alphascreen:
    """
    Class to handle images with alphascreen regions and insert
    other images or videos on it.
    """
    image = None
    image_filename: str = None
    alpha_regions = []

    def __init__(self, filename: str):
        if not isinstance(filename, str):
            raise Exception(f'No str "filename" parameter "{filename}" provided.')
        
        if not is_valid_image(filename):
            raise Exception(f'The provided "filename" parameter "{filename}" is not a valid image.')
        
        image = Image.open(filename)

        if not has_transparency(image):
            raise Exception('The provided image "filename" parameter "{filename}" does not have any alpha channel.')

        self.image_filename = filename
        self.image = image
        self.alpha_regions = ImageRegionFinder.find_transparent_regions(self.image)

        if len(self.alpha_regions) == 0:
            raise Exception('No alpha regions found in the "filename" parameter "{filename}" provided.')
        
        # TODO: What about regions that are just one pixel or too short (?)

    def insert_images(self, images, duration: float):
        """
        This method returns a CompositeVideoClip with the provided
        'images' fitting the different alphascreen areas and
        centered on those areas by applying a mask that let them be
        seen through that mask.
        """
        if len(images) > len(self.alpha_regions):
            raise Exception(f'There are more images provided ({str(len(images))}) than available alphascreen regions ({str(len(self.alpha_regions))}).')
        
        # TODO: Validate 'image' parameter properly
        for image in images:
            videos = ImageClip(image, duration = duration)

        return self.insert_videos(videos)

    def insert_image(self, image, duration: float):
        """
        This method returns a CompositeVideoClip with the provided
        'image' fitting the first alphascreen area and centered on
        those areas by applying a mask that let them be seen
        through that mask.
        """
        return self.insert_images([image], duration)
    
    def insert_videos(self, videos):
        """
        This method returns a CompositeVideoClip with the provided
        'videos' fitting the different alphascreen areas and
        centered on those areas by applying a mask that let them be
        seen through that mask.
        """
        if len(videos) > len(self.alpha_regions):
            raise Exception(f'There are more videos provided ({str(len(videos))}) than available alphascreen regions ({str(len(self.alpha_regions))}).')

        for video in videos:
            video = VideoParser.to_moviepy(video)

        for index, video in enumerate(videos):
            alpha_region = self.alpha_regions[index]
            videos[index] = self.set_video_size_to_fit_alphascreen_region(video, alpha_region)

            # We position it in the center of the alphascreen region
            x = (alpha_region['bottom_right'][0] + alpha_region['top_left'][0]) / 2 - videos[index].w / 2
            y = (alpha_region['bottom_right'][1] + alpha_region['top_left'][1]) / 2 - videos[index].h / 2
            # TODO: Cropping the video would be interesting to avoid being diplayed
            # over other videos if more than one alpha region and stranges aspect
            # ratios
            # from moviepy.video.fx.all import crop
            # videos[index] = crop(videos[index], x1 = alpha_region['top_left'][0], y1 = alpha_region['top_left'][1], x2 = alpha_region['bottom_right'][0], y2 = alpha_region['bottom_right'][1])
            videos[index] = videos[index].set_position((x, y))

        alphascreen_clip = ImageClip(self.image_filename, duration = video.duration)

        composite_clip = CompositeVideoClip([
            *videos,
            alphascreen_clip
        ], size = alphascreen_clip.size)

        return composite_clip

    def insert_video(self, video):
        """
        This method returns a CompositeVideoClip with the provided
        'video' fitting in the alphascreen area and centered on it
        by applying a mask that let it be seen through that mask.
        """
        return self.insert_videos([video])
    
    def set_video_size_to_fit_alphascreen_region(self, video, region):
        """
        This method rescales the provided 'video' to make it fit in
        the alphascreen region. Once it's been rescaled, this video
        should be placed in the center of the alphascreen region.
        """
        video = VideoParser.to_moviepy(video)

        # We have the alphascreen area corners and video corners
        alphascreen_width = region['bottom_right'][0] - region['top_left'][0]
        alphascreen_height = region['bottom_right'][1] - region['top_left'][1]

        video = resize_video(video, (alphascreen_width, alphascreen_height))
        
        # x, y = resize_to_fit_on_region((video.w, video.h), (alphascreen_width, alphascreen_height))
        # video = video.resize((x, y))

        return video