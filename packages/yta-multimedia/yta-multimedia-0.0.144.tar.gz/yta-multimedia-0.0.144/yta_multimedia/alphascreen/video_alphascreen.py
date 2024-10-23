from yta_multimedia.video.parser import VideoParser
from yta_multimedia.video.frames import VideoFrameExtractor
from yta_multimedia.alphascreen.masked_clip_creator import MaskedClipCreator
from yta_multimedia.video.edition.duration import set_video_duration, ExtendVideoMode
from yta_general_utils.image.parser import ImageParser
from yta_general_utils.image.region import ImageRegionFinder, Region
from moviepy.editor import ImageClip, CompositeVideoClip
from PIL import Image


class VideoAlphascreen:
    """
    Class to handle videos with alphascreen regions and insert
    other videos or images on it.
    """
    video = None
    alpha_regions: list[Region] = []

    def __init__(self, video: str):
        video = VideoParser.to_moviepy(video, has_mask = True)

        # TODO: Check that video mask has some transparency

        self.video = video
        # TODO: Import from 'frames' the 'get_frame_from_video_as_rgba_by_frame_number(0)'
        self.alpha_regions = ImageRegionFinder.find_transparent_regions(VideoFrameExtractor.get_frame_as_rgba_by_time(video, 0))

        if len(self.alpha_regions) == 0:
            raise Exception('No alpha regions found in the "filename" parameter "{filename}" provided.')
        
        # TODO: What about regions that are just one pixel or too short (?)

        alpha_clip = self.video
        self.masked_clip_creator = MaskedClipCreator(self.alpha_regions, alpha_clip)

    def from_image_to_image(self, image, output_filename: str = None):
        """
        This method returns a numpy representation of the image
        built by inserting the provided 'image' in this alphascreen.

        This method will write the result as a local file if the
        'output_filename' parameter is provided.

        This method will work if the amount of images to insert is
        the same of the amount of transparent regions existing in 
        this alphascreen.
        """
        return self.masked_clip_creator.from_image_to_image(image, output_filename)

        return self.from_images_to_image([image], output_filename)
    
    def from_images_to_image(self, images, output_filename: str = None):
        """
        This method returns a numpy representation of the image
        built by inserting the provided 'images' in this
        alphascreen.

        This method will write the result as a local file if the
        'output_filename' parameter is provided.

        This method will work if the amount of images to insert is
        the same of the amount of transparent regions existing in 
        this alphascreen.
        """
        return self.masked_clip_creator.from_images_to_image(images, output_filename)

        video = self.from_images_to_video(images, duration = 1 / 60)

        if output_filename:
            video.save_frame(output_filename, t = 0)

        return video.get_frame(t = 0)
    
    def from_image_to_video(self, image, duration: float, output_filename: str = None):
        """
        This method returns a CompositeVideoClip with the provided
        'image' fitting the first alphascreen area and centered on
        those areas by applying a mask that let them be seen
        through that mask.

        This method will write the result as a local file if the
        'output_filename' parameter is provided.

        This method will work if the amount of images to insert is
        the same of the amount of transparent regions existing in 
        this alphascreen.
        """
        return self.masked_clip_creator.from_image_to_video(image, duration, output_filename)

        return self.from_images_to_video([image], duration, output_filename)

    def from_images_to_video(self, images, duration: float, output_filename: str = None):
        """
        This method returns a CompositeVideoClip with the provided
        'images' fitting the different alphascreen areas and
        centered on those areas by applying a mask that let them be
        seen through that mask.

        This method will write the result as a local file if the
        'output_filename' parameter is provided.

        This method will work if the amount of images to insert is
        the same of the amount of transparent regions existing in 
        this alphascreen.
        """
        return self.masked_clip_creator.from_images_to_video(images, duration, output_filename)

        self.validate_enough_elements_for_regions(videos)

        for image in images:
            image = ImageParser.to_numpy(image)
        
        videos = []
        for image in images:
            videos.append(ImageClip(image, duration = duration).set_fps(60))

        return self.from_videos_to_video(videos, output_filename)
    
    def from_video_to_video(self, video, output_filename: str = None):
        """
        This method returns a CompositeVideoClip with the provided
        'video' fitting in the alphascreen area and centered on it
        by applying a mask that let it be seen through that mask.

        This method will write the result as a local file if the
        'output_filename' parameter is provided.

        This method will work if the amount of images to insert is
        the same of the amount of transparent regions existing in 
        this alphascreen.
        """
        return self.masked_clip_creator.from_video_to_video(video, output_filename)

        return self.from_videos_to_video([video], output_filename)
    
    def from_videos_to_video(self, videos, output_filename: str = None):
        """
        This method returns a CompositeVideoClip with the provided
        'videos' fitting the different alphascreen areas and
        centered on those areas by applying a mask that let them be
        seen through that mask.

        This method will write the result as a local file if the
        'output_filename' parameter is provided.

        This method will work if the amount of images to insert is
        the same of the amount of transparent regions existing in 
        this alphascreen.
        """
        return self.masked_clip_creator.from_videos_to_video(videos, output_filename)

        self.validate_enough_elements_for_regions(videos)

        for video in videos:
            video = VideoParser.to_moviepy(video)

        for index, video in enumerate(videos):
            alpha_region = self.alpha_regions[index]
            videos[index] = alpha_region.place_video_inside(video)

        return self.build_composite_clip(videos, self.video)
    
    def validate_enough_elements_for_regions(self, elements):
        """
        Raises an exception if the provided amount of 'elements' is 
        greater or less than the amount of alpha regions.
        """
        if len(elements) > len(self.alpha_regions) or len(elements) < len(self.alpha_regions):
            raise Exception(f'There are more or less elements provided ({str(len(elements))}) than available alphascreen regions ({str(len(self.alpha_regions))}).')

    def build_composite_clip(self, videos, alpha_clip, output_filename: str = None):
        """
        Builds the CompositeVideoClip that includes the provided 'videos'
        and the also provided 'alpha_clip' to build the desired video with
        alpha regions filled with the videos.
        """
        # TODO: Please private method
        # As this is for internal use I consider that 'videos' and
        # 'alpha_clip' are valid ones and ready to be used at this point

        # TODO: Provided videos can be shorther than the alphascreen
        # or the alphascreen can be shorter than the videos, so we
        # need an strategy to follow. By now I'm forcing all the 
        # videos to fit the alphascreen duration by shortening or
        # enlarging them.
        for index, _ in enumerate(videos):
            videos[index] = set_video_duration(videos[index], alpha_clip.duration, ExtendVideoMode.FREEZE_LAST_FRAME)

        composite_clip = CompositeVideoClip([
            *videos,
            alpha_clip
        ], size = alpha_clip.size)

        if not composite_clip.fps:
            composite_clip = composite_clip.set_fps(60)

        if output_filename:
            composite_clip.write_videofile(output_filename)

        return composite_clip