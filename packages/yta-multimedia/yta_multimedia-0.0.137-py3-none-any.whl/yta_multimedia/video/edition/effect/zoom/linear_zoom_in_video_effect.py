from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from yta_multimedia.video.edition.effect.utils.resize_t_functions import linear_zoom_in_t_func
from moviepy.editor import CompositeVideoClip, VideoFileClip, ImageClip, VideoClip, ColorClip
from typing import Union


class LinearZoomInVideoEffect(VideoEffect):
    """
    Creates a linear Zoom in effect in the provided video.
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], zoom_ratio = None):
        """
        Applies the effect on the provided 'video'.
        """
        video = VideoEffect.parse_moviepy_video(video)
        # We reset the mask to avoid problems with zoom
        video = video.add_mask()

        if zoom_ratio is None:
            zoom_ratio = 0.2

        fps = video.fps
        duration = video.duration
        screensize = video.size

        effected_video = (
            video
            .resize(screensize)
            .resize(lambda t: linear_zoom_in_t_func(t, duration, zoom_ratio))
            .set_position(('center', 'center'))
            .set_duration(duration)
            .set_fps(fps)
        )

        return CompositeVideoClip([effected_video], size = screensize)