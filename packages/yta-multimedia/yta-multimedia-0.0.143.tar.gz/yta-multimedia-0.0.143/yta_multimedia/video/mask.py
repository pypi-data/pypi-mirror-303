from yta_general_utils.file.checker import file_is_video_file
from yta_general_utils.file import list
from yta_general_utils.temp import create_custom_temp_filename 
from yta_multimedia.video.frames import get_frame_from_video_mask_by_frame_number, get_frame_from_video_by_frame_number
from moviepy.editor import VideoFileClip, ImageClip, concatenate_videoclips, CompositeVideoClip
from typing import Union

import numpy as np
import cv2


def invert_video_mask(video: Union[str, VideoFileClip]):
    """
    This method will invert the provided video mask. Make 
    sure the video you provide has a mask. This method 
    will return a mask containing the original video
    with the mask inverted.

    This method will iterate over each frame and will
    invert the numpy array to invert the opacity by 
    chaging the zeros by ones and the ones by zeros (but
    in 0 - 255 range).

    This is useful to overlay videos that have alpha 
    channels so they can let see the video behind through
    that alpha channel. For example, if your video is 
    just a manim animation with only text in the middle,
    the other pixels in the video will be alpha, so if you
    invert them you will obtain the text-transparent 
    effect that is a pretty artistic one.

    This mask has to be used in a specific way, that is in
    a CompositeVideoClip, in second position, with the
    'use_bgclip = True' flag to be over the other video.
    """
    # TODO: Check if video extension has a mask
    if not video:
        raise Exception('No "video" provided.')
    
    if isinstance(video, str):
        if not file_is_video_file:
            raise Exception('Provided "video" is not a valid video file.')
        
        video = VideoFileClip(video, has_mask = True)

    # We force to read a mask
    if not video.mask:
        video = VideoFileClip(video.filename, has_mask = True)

    # TODO: Confirm that this exist or create it if not
    FRAMES_FOLDER_NAME = 'frames_main'
    # This is to avoid memory limit exceeded
    in_memory = False

    # We will invert all frames
    # TODO: Please, try to do this with ffmpeg concatenate
    # images with alpha channel to video because it will be
    # faster but I couldn't in the past
    clips = []
    for i in range(int(video.fps * video.duration)):
        # TODO: Build my own utils method (?)
        mask_frame = get_frame_from_video_mask_by_frame_number(video, i)
        #mask_frame = video.mask.get_frame(i / 60)
        frame = get_frame_from_video_by_frame_number(video, i)

        # Invert the mask
        where_0 = np.where(mask_frame == 0)
        where_1 = np.where(mask_frame == 1)
        mask_frame[where_0] = 255
        mask_frame[where_1] = 0

        # Combine the fourth (alpha) channel
        mask_frame = mask_frame[:, :, np.newaxis]
        frame_rgba = np.concatenate((frame, mask_frame), axis = 2)
        if in_memory:
            clips.append(ImageClip(frame_rgba, duration = 1 / 60))
        else:
            tmp_frame_name = create_custom_temp_filename(FRAMES_FOLDER_NAME + '/frame' + str(i).zfill(5) + '.png')
            cv2.imwrite(tmp_frame_name, frame_rgba)
    
    if not in_memory:
        frames_folder = create_custom_temp_filename(FRAMES_FOLDER_NAME + '/')
        images = list(frames_folder, pattern = '*.png')
        for image in images:
            clips.append(ImageClip(image, duration = 1 / 60))

    mask = concatenate_videoclips(clips)

    return mask

# TODO: I think this will be deleted in the future, when refactored
# and when we confirm that here is another way of handling this
def apply_inverted_mask(video: Union[str, VideoFileClip], mask_video: Union[str, VideoFileClip], output_filename: Union[str, None] = None):
    """
    Applies the provided 'mask_video' with its mask inverted
    over the also provided 'video'. This is useful to make
    artistic effects. This methods applies the 
    'invert_video_mask' method to the provided 'mask_video'.
    """
    if not video:
        raise Exception('No "video" provided.')
    
    if not mask_video:
        raise Exception('No "mask_video" provided.')
    
    if isinstance(video, str):
        if not file_is_video_file:
            raise Exception('Provided "video" is not a valid video file.')
        
        video = VideoFileClip(video, has_mask = True)

    if isinstance(mask_video, str):
        if not file_is_video_file:
            raise Exception('Provided "mask_video" is not a valid video file.')
        
        mask_video = VideoFileClip(mask_video, has_mask = True)

    if not mask_video.mask:
        mask_video = VideoFileClip(mask_video.filename, has_mask = True)

    mask_video = invert_video_mask(mask_video)
    # TODO: Handle durations
    final_clip = CompositeVideoClip([video, mask_video.subclip(0, video.duration)], use_bgclip = True)
    final_clip = final_clip.set_audio(video.audio)

    if output_filename:
        final_clip.write_videofile(output_filename)

    return final_clip

# TODO: Look for the way to store the video with the inverted mask locally
# so I can use that video as usual. Normally I download video with alpha
# layers from the Internet or I create them with manim, but now I have to
# handle it manually, so this is a challenge