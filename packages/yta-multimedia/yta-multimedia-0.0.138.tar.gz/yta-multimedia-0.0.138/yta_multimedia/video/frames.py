from moviepy.editor import VideoFileClip
from yta_general_utils.checker.type import variable_is_type
from yta_general_utils.file.checker import file_is_video_file
from typing import Union


def get_all_frames_from_video(video: Union[VideoFileClip, str], output_folder: Union[str, None] = None):
    """
    This method will get all the frames of the provided 'video' and
    will return them. It 'output_folder' is provided, they will be
    also stored locally in that folder with the 'frameXXXXX.png' 
    name, from 0 to the last frame that exist.

    @param
        **video**
        The video from which we want to get all the frames
    """
    if not video:
        return None
    
    if output_folder and not output_folder.endswith('/'):
        output_folder += '/'
    
    if variable_is_type(video, str):
        if not file_is_video_file(video):
            return None
        
        video = VideoFileClip(video)

    # TODO: Maybe enhance this by first getting them and writing
    # manually with other method, and then returning
    if output_folder:
        video.write_images_sequence(output_folder + 'frame%05d.png')

    frame_numbers = [i for i in range((int) (video.fps * video.duration))]

    return get_frames_from_video_by_frame_numbers(video, frame_numbers)

# TODO: This method should be in another place as its behaviour is
# very different as the single one below. This is for summarizing
# a video or to help other functionalities like that
def get_frames_from_video_by_frame_numbers(video: Union[VideoFileClip, str], frame_numbers = [], output_folder: str = None):
    """
    This method will obtain the frame corresponding to the provided
    'frame_numbers' of the also provided 'video'. They will be 
    returned and if 'output_folder' is given, they will be stored
    locally. Each of the frames is a np.ndarray.

    @param
        **frame_numbers**
        A list containing the frame numbers we want to get, that 
        need to be available in the provided 'video'.
    """
    if not video:
        return None
    
    # TODO: Check 'frame_numbers' better
    if len(frame_numbers) == 0:
        return None
    
    if output_folder and not output_folder.endswith('/'):
        output_folder += '/'
    
    if variable_is_type(video, str):
        if not file_is_video_file(video):
            return None
        
        video = VideoFileClip(video)

    # Obtain the max frame number and check if it is available
    if max(frame_numbers) > ((int) (video.fps * video.duration)):
        raise Exception('Some frame requested does not exist in the provided video.')
    
    frames = []
    for frame_number in frame_numbers:
        output_filename = None
        if output_folder:
            output_filename = 'frame' + str(frame_number).zfill(5) + '.png'
        frames.append(get_frame_from_video_by_frame_number(video, frame_number, output_filename))
        
    return frames

def get_frame_from_video_by_frame_number(video: Union[VideoFileClip, str], frame_number: int, output_filename: Union[str, None] = None):
    """
    Extracts the frame 'frame_number' from the provided 'video' that will
    be stored locally as 'output_filename' if that parameter is provided
    or will not if it is None. This method will return the frame as 
    np.ndarray.

    @param
        **video**
        The video from which you want to get the frame.

    @param
        **frame_number**
        The frame that you want to extract from the video. This must be
        an int. If you want to get the first frame, this parameter must
        be 0. If you want to get the 26th frame, pass 26 as parameter.

    @param
        **output_filename**
        The name to store the frame locally. None value will make being
        not stored, only returned.
    """
    if not video:
        return None
    
    if frame_number < 0:
        return None
    
    if variable_is_type(video, str):
        if not file_is_video_file(video):
            return None
        
        video = VideoFileClip(video)

    if frame_number > (int) (video.fps * video.duration):
        return None

    return get_frame_from_video_by_time(video, frame_number * 1.0 / video.fps, output_filename)

def get_frame_from_video_by_time(video: Union[VideoFileClip, str], time: float, output_filename: str = None):
    """
    Extracts a frame from the provided 'video' that is exactly at the
    also provided 'time' moment. The frame will be stored as 
    'output_filename'. This will return the frame as np.ndarray.

    @param
        **time**
        The moment of the clip in which the frame is shown. This should be
        something like "frame_number * 1.0 / self.video.fps" to work well.
        Passing 0 will return the first frame of the video, and passing 2
        will return the frame in the second 2 of the video.
    """
    if not video:
        return None
    
    if time < 0:
        return None
    
    if variable_is_type(video, str):
        if not file_is_video_file(video):
            return None
        
        video = VideoFileClip(video)

    if time > video.duration:
        return None
    
    if output_filename:
        video.save_frame(t = time, filename = output_filename)

    return video.get_frame(t = time)

def get_all_mask_frames_from_video(video: Union[VideoFileClip, str], output_folder: Union[str, None] = None):
    """
    This method will get all the frames of the provided 'video'
    mask and will return them. It 'output_folder' is provided,
    they will be also stored locally in that folder with the 
    'frameXXXXX.png' name, from 0 to the last frame that exist.

    @param
        **video**
        The video from which we want to get all the mask frames
    """
    if not video:
        return None
    
    if output_folder and not output_folder.endswith('/'):
        output_folder += '/'
    
    if variable_is_type(video, str):
        if not file_is_video_file(video):
            return None
        
        video = VideoFileClip(video, has_mask = True)

    if not video.mask:
        video = VideoFileClip(video.filename, has_mask = True)

    # TODO: Maybe enhance this by first getting them and writing
    # manually with other method, and then returning
    if output_folder:
        video.mask.write_images_sequence(output_folder + 'frame%05d.png')

    frame_numbers = [i for i in range((int) (video.fps * video.duration))]

    # Due to some changes on 14th october 2024 this could be working not
    return get_frames_with_mask_from_video_by_frame_numbers(video.mask, frame_numbers)

# TODO: This method should be in another place as its behaviour is
# very different as the single one below. This is for summarizing
# a video or to help other functionalities like that
def get_frames_with_mask_from_video_by_frame_numbers(video: Union[VideoFileClip, str], frame_numbers = [], output_folder: str = None):
    """
    This method will obtain the frame corresponding to the provided
    'frame_numbers' of the also provided 'video' mask. They will be 
    returned and if 'output_folder' is given, they will be stored
    locally. Each of the frames is a np.ndarray.

    @param
        **frame_numbers**
        A list containing the frame numbers we want to get, that 
        need to be available in the provided 'video' mask.
    """
    if not video:
        return None
    
    # TODO: Check 'frame_numbers' better
    if len(frame_numbers) == 0:
        return None
    
    if output_folder and not output_folder.endswith('/'):
        output_folder += '/'
    
    if variable_is_type(video, str):
        if not file_is_video_file(video):
            return None
        
        video = VideoFileClip(video, has_mask = True)

    # Obtain the max frame number and check if it is available
    if max(frame_numbers) > ((int) (video.fps * video.duration)):
        raise Exception('Some frame requested does not exist in the provided video.')
    
    if not video.mask:
        video.add_mask()

    return get_frames_from_video_by_frame_numbers(video.mask, frame_numbers, output_folder)

def get_frame_from_video_mask_by_frame_number(video: Union[VideoFileClip, str], frame_number: int, output_filename: Union[str, None] = None):
    """
    Extracts the frame 'frame_number' from the provided 'video' mask 
    that will be stored locally as 'output_filename' if that parameter
    is provided or will not if it is None. This method will return the
    mask frame as np.ndarray.

    Please, provide a video that contains a valid mask, or the 
    result will be useless. This method will force the 'has_mask'
    attribute to obtain the mask, but if the video has no 
    transparency this method doesn't make sense.

    @param
        **video**
        The video from which you want to get the mask frame.

    @param
        **frame_number**
        The frame that you want to extract from the video. This must be
        an int. If you want to get the first frame, this parameter must
        be 0. If you want to get the 26th frame, pass 26 as parameter.

    @param
        **output_filename**
        The name to store the mask frame locally. None value will make
        being not stored, only returned.
    """
    if not video:
        return None
    
    if frame_number < 0:
        return None
    
    if variable_is_type(video, str):
        if not file_is_video_file(video):
            return None
        
        video = VideoFileClip(video, has_mask = True)

    if not video.mask:
        video = VideoFileClip(video.filename, has_mask = True)

    if frame_number > (int) (video.fps * video.duration):
        return None

    return get_frame_from_video_mask_by_time(video, frame_number * 1.0 / video.fps, output_filename)

def get_frame_from_video_mask_by_time(video: Union[VideoFileClip, str], time: float, output_filename: str = None):
    """
    Extracts a frame from the provided 'video' mask that is exactly 
    at the also provided 'time' moment. The mask frame will be 
    stored as 'output_filename'. This will return the frame as 
    np.ndarray.

    Please, provide a video that contains a valid mask, or the 
    result will be useless. This method will force the 'has_mask'
    attribute to obtain the mask, but if the video has no 
    transparency this method doesn't make sense.

    @param
        **time**
        The moment of the clip in which the frame is shown. This should be
        something like "frame_number * 1.0 / self.video.fps" to work well.
        Passing 0 will return the first frame of the video, and passing 2
        will return the frame in the second 2 of the video.
    """
    if not video:
        return None
    
    if time < 0:
        return None
    
    if variable_is_type(video, str):
        if not file_is_video_file(video):
            return None
        
        video = VideoFileClip(video, has_mask = True)

    if time > video.duration:
        return None
    
    if not video.mask:
        video = VideoFileClip(video.filename, has_mask = True)

    return get_frame_from_video_by_time(video.mask, time, output_filename)

    if output_filename:
        video.mask.save_frame(t = time, filename = output_filename)

    return video.mask.get_frame(t = time)