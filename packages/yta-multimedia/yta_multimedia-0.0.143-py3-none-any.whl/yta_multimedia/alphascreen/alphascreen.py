from yta_multimedia.video.parser import VideoParser
from yta_multimedia.video.edition.resize import resize_video
from yta_multimedia.image.edition.resize import resize_image
from yta_general_utils.image.parser import ImageParser
from yta_general_utils.image.checker import has_transparency
from yta_general_utils.file.checker import is_valid_image
from yta_general_utils.image.region import ImageRegionFinder, Region
from moviepy.editor import ImageClip, CompositeVideoClip
from PIL import Image


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
        if len(images) > len(self.alpha_regions) or len(images) < len(self.alpha_regions):
            raise Exception(f'There are more or less images provided ({str(len(images))}) than available alphascreen regions ({str(len(self.alpha_regions))}).')

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
        if len(videos) > len(self.alpha_regions) or len(videos) < len(self.alpha_regions):
            raise Exception(f'There are more or less videos provided ({str(len(videos))}) than available alphascreen regions ({str(len(self.alpha_regions))}).')

        for video in videos:
            video = VideoParser.to_moviepy(video)

        for index, video in enumerate(videos):
            alpha_region = self.alpha_regions[index]
            videos[index] = alpha_region.resize_video_to_fit_in(video)
            #videos[index] = self.set_video_size_to_fit_region(video, alpha_region)

            # I need one AR extra pixel each side to ensure there are no black parts

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

        if not composite_clip.fps:
            composite_clip = composite_clip.set_fps(60)

        if output_filename:
            composite_clip.write_videofile(output_filename)

        return composite_clip
    
    # TODO: This has been moved to yta_general_utils\image\region.py
    # TODO: Is this method actually used (?)
    def set_image_size_to_fit_region(self, image, region: Region):
        """
        This method rescales the provided 'image' to make it fit in
        the alphascreen region. Once it's been rescaled, this image
        should be placed in the center of the alphascreen region.
        """
        image = ImageParser.to_pillow(image)

        # We have the alphascreen area corners and video corners
        region_w = region.bottom_right.x - region.top_left.x
        region_h = region.bottom_right.y - region.top_left.y

        image = resize_image(image, (region_w, region_h))
        # We enlarge it a 1% to avoid some balck pixels lines
        image = image.resize((image.size[0] * 1.01, image.size[1] * 1.01))

        return image
    
    def set_video_size_to_fit_region(self, video, region: Region):
        """
        This method rescales the provided 'video' to make it fit in
        the alphascreen region. Once it's been rescaled, this video
        should be placed in the center of the alphascreen region.
        """
        video = VideoParser.to_moviepy(video)

        # We have the alphascreen area corners and video corners
        region_w = region.bottom_right.x - region.top_left.x
        region_h = region.bottom_right.y - region.top_left.y

        video = resize_video(video, (region_w, region_h))
        # We enlarge it a 1% to avoid some black pixels lines
        video = video.resize(1.01)

        return video