from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from yta_multimedia.video.frames import VideoFrameExtractor
from moviepy.editor import CompositeVideoClip, VideoFileClip, ImageClip, concatenate_videoclips, VideoClip, ColorClip
from typing import Union


class StopMotionVideoEffect(VideoEffect):
    """
    Creates a Stop Motion effect in the provided video by dropping the frames
    per second but maintaining the original frames ratio.
    """
    
    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip]):
        """
        Applies the effect on the provided 'video'.
        """
        video = VideoEffect.parse_moviepy_video(video)

        FRAMES_TO_JUMP = 5

        clips = []
        for frame_number in range((int) (video.fps * video.duration)):
            if frame_number % FRAMES_TO_JUMP == 0:
                frame = VideoFrameExtractor.get_frame_by_frame_number(video, frame_number)
                clips.append(ImageClip(frame, duration = FRAMES_TO_JUMP / video.fps).set_fps(video.fps))

        return concatenate_videoclips(clips).set_audio(video.audio).set_fps(video.fps)


    