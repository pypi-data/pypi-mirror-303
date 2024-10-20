from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from yta_multimedia.video.edition.effect.utils.resize_t_functions import linear_zoom_transition_t_func
from moviepy.editor import CompositeVideoClip, VideoFileClip, ImageClip, VideoClip, ColorClip
from typing import Union


class LinearZoomVideoEffect(VideoEffect):
    """
    Creates a linear Zoom effect in the provided video.
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], zoom_start: float, zoom_end: float):
        """
        Applies the effect on the provided 'video'.
        """
        video = VideoEffect.parse_moviepy_video(video)
        # We reset the mask to avoid problems with zoom
        video = video.add_mask()

        if not zoom_start or not zoom_end:
            raise Exception('No "zoom_start" or "zoom_end" provided.')

        fps = video.fps
        duration = video.duration
        screensize = video.size

        effected_video = (
            video
            .resize(screensize)
            .resize(lambda t: linear_zoom_transition_t_func(t, duration, zoom_start, zoom_end))
            .set_position(('center', 'center'))
            .set_duration(duration)
            .set_fps(fps)
        )

        return CompositeVideoClip([effected_video], size = screensize)


    