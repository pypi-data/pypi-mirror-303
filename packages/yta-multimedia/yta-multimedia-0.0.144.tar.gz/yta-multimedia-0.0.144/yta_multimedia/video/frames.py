"""
Using the 'get_frame' in moviepy returns a numpy array of 3 or 1 
dimension depending on the type of clip. If the clip is a main 
clip, a 3d array with values between [0, 255] is returned (one
[255, 255, 255] array would be a white pixel). If the clip is a
mask clip, a 1d array with values between [0, 1] is returned (the
1 completely transparent, the 0 is not).

Thats why you need to normalize or denormalize those values to
work with them because they are different and turning frames into
an image would need you to have the same range [0, 1] or [0, 255].

Check the Pillow, ImageIO and other libraries to see what kind of
numpy arrays are needed to write (or read) images.
"""
from yta_multimedia.video.parser import VideoParser
from yta_general_utils.programming.enum import YTAEnum as Enum
from yta_general_utils.checker.type import variable_is_positive_number
from imageio import imsave

import numpy as np


class FrameExtractionType(Enum):
    TIME = 'time'
    FRAME_NUMBER = 'frame_number'

class VideoFrameExtractor:
    """
    Class to simplify the process of extracting video frames by time
    or frame number.
    """
    # TODO: Implement the 'output_filename' optional parameter to store
    # the frames if parameter is provided.
    @classmethod
    def _get_frame_time(cls, video, frame_number_or_time, extraction_type: FrameExtractionType):
        """
        Returns the time to obtain the frame of the provided 'video'
        according to the provided 'frame_number_or_time' parameter and
        the desired 'extraction_type'.

        This method is useful to be used first to validate that the
        frame times or numbers are valid and avoid getting all the 
        frames and loading them in memory if it is going to fail.
        """
        video = VideoParser.to_moviepy(video)
        extraction_type = FrameExtractionType.to_enum(extraction_type)
        
        if not frame_number_or_time or not variable_is_positive_number(frame_number_or_time):
            raise Exception('The provided "frame_number_or_time" is not a valid number.')
        
        if extraction_type == FrameExtractionType.FRAME_NUMBER:
            max_frame_number = video.fps * video.duration
            if frame_number_or_time > max_frame_number:
                raise Exception(f'The provided "frame_number" parameter {str(frame_number_or_time)}" is not valid. The maximum is {str(max_frame_number)}.')
            
            frame_number_or_time = frame_number_or_time * 1.0 / video.fps
        elif extraction_type == FrameExtractionType.TIME:
            if frame_number_or_time > video.duration:
                raise Exception(f'The provided "time" parameter {str(frame_number_or_time)} is not valid. The maximum is {str(video.duration)}.')
            
        return frame_number_or_time

    # TODO: I think I won't use this because I need to validate them first
    @classmethod
    def _get_frame(cls, video, frame_number_or_time, extraction_type: FrameExtractionType, output_filename: str):
        """
        Returns the frame of the provided 'video' according to the provided
        'frame_number_or_time' parameter and the desired 'extraction_type'.
        """
        video = VideoParser.to_moviepy(video)

        frame = video.get_frame(t = cls._get_frame_time(video, frame_number_or_time, extraction_type))

        if output_filename:
            cls._save_frame(frame, output_filename)

        return frame
    
    @classmethod
    def _get_frames(cls, video, frame_numbers_or_times, extraction_type: FrameExtractionType):
        """
        This method validates if all the provided 'frame_numbers_or_times'
        array parameter items are valid or not and them get all the frames
        and returns them as an array. This is optimum as it doesn't load
        frames until it's been verified the condition that all are valid.
        """
        # Validate and get all times to obtain the frames later
        times = [cls._get_frame_time(video, frame_number_or_time, extraction_type) for frame_number_or_time in frame_numbers_or_times]

        return [video.get_frame(t = time) for time in times]
    
    @classmethod
    def get_frames_by_time(cls, video, times: list[float]):
        """
        Returns the frames (as numpy arrays) from the provided 'video'
        that corresponds to the provided 'times' time momnets of the
        video.

        This method will raise an Exception if the limits are not valid
        for the given 'video'.
        """
        frames =  cls._get_frames(video, times, FrameExtractionType.TIME)

        return frames

    @classmethod
    def _save_frame(cls, frame, output_filename: str):
        if not output_filename:
            return None
        
        # TODO: Validate 'output_filename'
        
        # TODO: This is how 'video.save_frame' works
        # https://github.com/Zulko/moviepy/blob/master/moviepy/video/VideoClip.py#L166
        # from imageio import imsave
        # im = self.get_frame(t)
        # if with_mask and self.mask is not None:
        #     mask = 255 * self.mask.get_frame(t)
        #     im = np.dstack([im, mask]).astype("uint8")
        # else:
        #     im = im.astype("uint8")

        imsave(output_filename, frame.astype("uint8"))

        return True

    @classmethod
    def get_frame_by_time(cls, video, time: float, output_filename: str):
        """
        Returns the frame (as numpy arrays) from the provided 'video'
        that corresponds to the provided 'time' moment.

        This method will raise an Exception if the limits are not valid
        for the given 'video'.
        """
        frame = cls.get_frames_by_time(video, [time])[0]

        if output_filename:
            cls._save_frame(frame, output_filename)

        return frame
    
    @classmethod
    def get_frames_by_time_from_start_to_end(cls, video, start_time: float, end_time: float):
        """
        Returns the frames (as numpy arrays) from the provided 'video'
        that corresponds to the lapse of time between the provided
        'start_time' and 'end_time'.

        This method will raise an Exception if the limits are not valid
        for the given 'video'.
        """
        video = VideoParser.to_moviepy(video)

        # Validate start and end parameters
        if not variable_is_positive_number(start_time) or start_time < 0 or start_time > video.duration:
            raise Exception(f'The provided "start_time" parameter "{str(start_time)}" is not valid. It must be a positive number between 0 and the video duration ({str(video.duration)}).')
        if not variable_is_positive_number(end_time) or end_time < 0 or end_time < start_time or end_time > video.duration:
            raise Exception(f'The provided "end_time" parameter "{str(end_time)}" is not valid. It must be a positive number between 0 and the video duration ({str(video.duration)}), and greater than the provided "start_time" parameter.')
        
        total_frames = int(video.duration * video.fps)
        time_moments = []
        for frame in range(total_frames):
            frame_time_moment = frame / video.fps  # tiempo en segundos para el frame actual
            if start_time <= frame_time_moment <= end_time:
                time_moments.append(frame_time_moment)

        return cls.get_frames_by_time(video, time_moments)

    @classmethod
    def get_frame_by_frame_number(cls, video, frame_number: int, output_filename: str):
        """
        Returns the frame (as numpy array) for the provided 'video' that
        corresponds to the provided 'frame_number'.

        This method will raise an Exception if the provided 'frame_number'
        is not a valid frame number for the given 'video'.
        """
        frame = cls._get_frame(video, frame_number, FrameExtractionType.FRAME_NUMBER)

        if output_filename:
            cls._save_frame(frame, output_filename)

        return frame
    
    @classmethod
    def get_frames_by_frame_number(cls, video, frame_numbers: list[int]):
        """
        Returns the frames (as numpy arrays) from the provided 'video'
        that corresponds to the provided 'frame_numbers'.

        This method will raise an Exception if the limits are not valid
        for the given 'video'.
        """
        return cls._get_frames(video, frame_numbers, FrameExtractionType.FRAME_NUMBER)
    
    @classmethod
    def get_frames_by_frame_number_from_start_to_end(cls, video, start_frame: float, end_frame: float):
        """
        Returns the frames (as numpy arrays) from the provided 'video' 
        from the 'start_frame' to the 'end_frame'.

        This method will raise an Exception if the limits are not valid
        for the given 'video'.
        """
        video = VideoParser.to_moviepy(video)

        max_frame_number = int(video.fps * video.duration)
        # Validate start and end parameters
        if not variable_is_positive_number(start_frame) or start_frame < 0 or start_frame > max_frame_number:
            raise Exception(f'The provided "start_frame" parameter "{str(start_frame)}" is not valid. It must be a positive number between 0 and the maximum frame ({str(max_frame_number)}).')
        if not variable_is_positive_number(end_frame) or end_frame < 0 or end_frame < start_frame or end_frame > max_frame_number:
            raise Exception(f'The provided "end_frame" parameter "{str(end_frame)}" is not valid. It must be a positive number between 0 and the maximum frame ({str(max_frame_number)}), and greater than the provided "start_time" parameter.')
        
        frames = [int(frame / video.fps) for frame in range(start_frame, end_frame + 1)]
        time_moments = [cls._get_frame_time(video, frame, FrameExtractionType.FRAME_NUMBER) for frame in frames]

        return cls.get_frames_by_time(video, time_moments)
    
    @classmethod
    def get_all_frames(cls, video):
        """
        Returns all the frames from the provided 'video'.
        """
        video = VideoParser.to_moviepy(video)

        # TODO: This was previously written in files like this:
        # if output_folder:
        #     video.write_images_sequence(output_folder + 'frame%05d.png')

        last_frame = (int) (video.duration * video.fps)

        return cls.get_frames_by_frame_number_from_start_to_end(video, 0, last_frame)
    
    # TODO: Would be perfect to have some methods to turn frames into
    # RGBA denormalized (0, 255) or normalized (0, 1) easier because
    # it is needed to work with images and other libraries. Those 
    # methods would iterate over the values and notice if they are in
    # an specific range so they need to be change or even if they are
    # invalid values (not even in [0, 255] range because they are not
    # rgb or rgba colors but math calculations).
    @classmethod
    def get_frame_as_rgba_by_time(cls, video, time: int, output_filename: str):
        """
        Gets the frame of the requested 'time' of the provided
        'video' as a normalized RGBA numpy array that is built
        by joining the rgb frame (from main clip) and the alpha
        (from .mask clip), useful to detect transparent regions.
        """
        video = VideoParser.to_moviepy(video, has_mask = True)
        
        main_frame = cls.get_frame_by_time(video, time) / 255  # RGB numpy array normalized 3d <= r,g,b
        mask_frame = cls.get_frame_by_time(video.mask, time)[:, :, np.newaxis]  # Alpha numpy array normalized 1d <= alpha

        # Combine RGB of frame and A from mask to RGBA numpy array
        frame_rgba = np.concatenate((main_frame, mask_frame), axis = 2) # 4d <= r,g,b,alpha

        if output_filename:
            # TODO: Write numpy as file image
            # Video mask is written as 0 or 1 (1 is transparent)
            # but main frame is written as 0 to 255, and the
            # 'numpy_image_to_pil' is expecting from 0 to 1
            # (normalized) instead of from 0 to 255 so it won't
            # work
            #from yta_general_utils.image.converter import numpy_image_to_pil
            pass

        return frame_rgba
