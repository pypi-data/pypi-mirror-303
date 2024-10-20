from yta_multimedia.video.utils import parse_parameter_as_moviepy_clip
from yta_general_utils.image.checker import has_transparency
from yta_general_utils.file.checker import is_valid_image
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
        self.alpha_regions = self.get_alpha_regions(self.image)

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
            video = parse_parameter_as_moviepy_clip(video)

        for index, video in enumerate(videos):
            alpha_region = self.alpha_regions[index]
            videos[index] = self.set_video_size_to_fit_alphascreen_region(video, alpha_region)

            # We position it in the center of the alphascreen region
            x = (alpha_region['bottom_right'][0] + alpha_region['top_left'][0]) / 2 - videos[index].w / 2
            y = (alpha_region['bottom_right'][1] + alpha_region['top_left'][1]) / 2 - videos[index].h / 2
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
        video = parse_parameter_as_moviepy_clip(video)

        # We have the alphascreen area corners and video corners
        alphascreen_width = region['bottom_right'][0] - region['top_left'][0]
        alphascreen_height = region['bottom_right'][1] - region['top_left'][1]

        # We force 16:9 scale ratio.
        # If we want to keep dimensions correctly, we will increase
        # (or decrease) the dimensions by these values below for each
        # step
        # TODO: This should be adapted to the actual aspect ratio, but
        # I want my videos to be 16:9
        STEP_X = 16 * 2
        STEP_Y = 9 * 2

        # If video is larger than alphascreen area, we need to make it
        # smaller. In any other case, bigger
        if video.w > alphascreen_width and video.h > alphascreen_height:
            STEP_X = -STEP_X
            STEP_Y = -STEP_Y

        do_continue = True
        tmp_size = [video.w, video.h]
        while (do_continue):
            tmp_size = [tmp_size[0] + STEP_X, tmp_size[1] + STEP_Y]

            if STEP_X < 0 and (tmp_size[0] < alphascreen_width or tmp_size[1] < alphascreen_height):
                # The previous step had the right dimensions
                tmp_size[0] += abs(STEP_X)
                tmp_size[1] += abs(STEP_Y)
                do_continue = False
            elif STEP_X > 0 and (tmp_size[0] > alphascreen_width and tmp_size[1] > alphascreen_height):
                # This step is ok
                do_continue = False

        video = video.resize((tmp_size[0], tmp_size[1]))

        return video

    @classmethod
    def get_alpha_regions(cls, image):
        """
        This method iterates through the provided image (image
        opened with PIL library Image.open()) and returns the
        'top_left' and 'bottom_right' corners (as [x, y]) of
        each alpha region found.

        This is useful to place another resources just in that
        position.

        This method will raise an Exception if the provided 
        'image' does not have any alpha pixel or is not an
        opened image with Image.open().
        """
        # The 8 directions in which we can move th check pixels
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        image = np.asarray(image)

        def is_valid(x, y, image, visited):
            """
            This method verifies if the pixel is between the limits
            and is transparent and unvisited.
            """
            rows, cols, _ = image.shape

            return (0 <= x < rows and 0 <= y < cols and not visited[x, y] and image[x, y, 3] == 0)

        def dfs(image, visited, x, y, region):
            """
            A Deep First Search algorithm applied to the image to 
            obtain all the pixels connected in a region.
            """
            stack = [(x, y)]
            visited[x, y] = True
            region.append((x, y))
            
            while stack:
                cx, cy = stack.pop()
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if is_valid(nx, ny, image, visited):
                        visited[nx, ny] = True
                        region.append((nx, ny))
                        stack.append((nx, ny))

        def is_inside(small_bounds, large_bounds):
            """
            This method verifies if the bounds of a found region are
            inside another bounds to discard the smaller regions.
            """
            min_x_small, max_x_small, min_y_small, max_y_small = small_bounds
            min_x_large, max_x_large, min_y_large, max_y_large = large_bounds
            
            return (
                min_x_small >= min_x_large and max_x_small <= max_x_large and
                min_y_small >= min_y_large and max_y_small <= max_y_large
            )

        def find_transparent_regions(image):
            """
            This method looks for all the existing regions of transparent
            pixels that are connected ones to the others (neighbours).
            """
            rows, cols, _ = image.shape
            visited = np.zeros((rows, cols), dtype=bool)
            regions = []
            
            for row in range(rows):
                for col in range(cols):
                    # If we find a transparent pixel, we search
                    if image[row, col, 3] == 0 and not visited[row, col]:
                        region = []
                        dfs(image, visited, row, col, region)
                        
                        if region:
                            min_x = min(px[0] for px in region)
                            max_x = max(px[0] for px in region)
                            min_y = min(px[1] for px in region)
                            max_y = max(px[1] for px in region)
                            
                            # These are the limits of the region
                            bounds = (min_x, max_x, min_y, max_y)
                            
                            # We need to avoid small regions contained in others
                            if not any(is_inside(bounds, r['bounds']) for r in regions):
                                regions.append({
                                    'bounds': bounds
                                })

            # I want another format, so:
            for index, region in enumerate(regions):
                regions[index] = {
                    # 'top_left': [region['bounds'][0], region['bounds'][2]],
                    # 'bottom_right': [region['bounds'][1], region['bounds'][3]]
                    # I don't know why I have to use it in this order but...
                    'top_left': [region['bounds'][2], region['bounds'][0]],
                    'bottom_right': [region['bounds'][3], region['bounds'][1]]
                }

            return regions
        
        return find_transparent_regions(image)