from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, AudioFileClip, ColorClip, vfx, VideoClip
from typing import Union
from yta_multimedia.resources.video.effect.sound.drive_urls import SAD_MOMENT_GOOGLE_DRIVE_DOWNLOAD_URL
from yta_multimedia.resources import get_resource
from yta_multimedia.video.edition.effect.constants import EFFECTS_RESOURCES_FOLDER


class SadMomentVideoEffect(VideoEffect):
    """
    This method gets the first frame of the provided 'clip' and returns a
    new clip that is an incredible 'sad_moment' effect with black and white
    filter, zoom in and rotating effect and also sad violin music.

    The 'duration' parameter is to set the returned clip duration, but the
    default value is a perfect one.
    """
    
    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip], duration = None):
        """
        Applies the effect to the provided 'video'.
        """
        video = VideoEffect.parse_moviepy_video(video)

        if not duration:
            duration = 4.8

        # We freeze the first frame
        aux = ImageClip(video.get_frame(0), duration = duration)
        aux.fps = video.fps
        video = aux

        # We then build the whole effect
        video = video.fx(vfx.blackwhite).resize(lambda t: 1 + 0.30 * (t / video.duration)).set_position(lambda t: (-(0.15 * video.w * (t / video.duration)), -(0.15 * video.h * (t / video.duration)))).rotate(lambda t: 5 * (t / video.duration), expand = False)

        # We set the effect audio
        TMP_FILENAME = get_resource(SAD_MOMENT_GOOGLE_DRIVE_DOWNLOAD_URL, EFFECTS_RESOURCES_FOLDER + 'sounds/sad_moment.mp3')
        video.audio = AudioFileClip(TMP_FILENAME).set_duration(video.duration)

        return CompositeVideoClip([
            ColorClip(color = [0, 0, 0], size = video.size, duration = video.duration),
            video,
        ])