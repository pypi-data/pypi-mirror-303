from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, VideoClip, ColorClip
from typing import Union
from skimage.filters import gaussian


class BlurVideoEffect(VideoEffect):
    """
    This effect will zoom out the clip, on the center.

    TODO: This effect is not smooth as it makes it have
    a black border. Maybe removing it (?)
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], blur_radius = None):
        """
        Applies the effect to the provided 'video'.
        """
        video = VideoEffect.parse_moviepy_video(video)

        if blur_radius is None:
            blur_radius = 4

        return video.fl(lambda get_frame, t: gaussian(get_frame(t).astype(float), sigma = blur_radius))
