from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from yta_multimedia.resources.video.effect.sound.drive_urls import PHOTO_GOOGLE_DRIVE_DOWNLOAD_URL
from yta_multimedia.video.edition.effect.moviepy.blink_video_effect import BlinkVideoEffect
from yta_multimedia.resources import get_resource
from yta_multimedia.video.edition.effect.constants import EFFECTS_RESOURCES_FOLDER
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, CompositeAudioClip, AudioFileClip, ColorClip, VideoClip
from typing import Union


class PhotoVideoEffect(VideoEffect):
    """
    Simulates that a photo is taken by making a white blink and
    a camera click sound. This effect doesn't freeze the video,
    it is just a white blink with a camera photo sound being
    played.
    """
    
    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip]):
        """
        Applies the effect to the provided 'clip'.
        """
        video = VideoEffect.parse_moviepy_video(video)

        TMP_FILENAME = get_resource(PHOTO_GOOGLE_DRIVE_DOWNLOAD_URL, EFFECTS_RESOURCES_FOLDER + 'sounds/photo_taken.mp3')

        # We force the effect to be last as much as the clip
        video = BlinkVideoEffect.apply(video, [255, 255, 255])

        effect_duration = 0.2
        if video.duration < effect_duration:
            effect_duration = video.duration

        video.audio = CompositeAudioClip([
            video.audio,
            AudioFileClip(TMP_FILENAME).set_duration(effect_duration)
        ])

        return video