from yta_multimedia.video.edition.effect.video_effect import VideoEffect
from yta_multimedia.video.frames import VideoFrameExtractor
from yta_general_utils.temp import create_temp_filename
from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, AudioFileClip, ImageSequenceClip, ColorClip, VideoClip
from typing import Union
from pydub import AudioSegment


class ReversedVideoEffect(VideoEffect):
    """
    This method creates a new one but in reversa, also with the sound reversed.

    It doesn't use the 'mirror_time' effect because it fails. Instead, it saves
    each frame of the video and builds a new video using them in reverse order.
    It also uses the original audio an reverses it in the new generated video.
    """

    @classmethod
    def apply(cls, video: Union[str, VideoFileClip, VideoClip, CompositeVideoClip, ImageClip, ColorClip]):
        """
        Applies the effect to the provided 'video'.
        """
        video = VideoEffect.parse_moviepy_video(video)

        reversed_frames_array = VideoFrameExtractor.get_all_frames(video)[::-1]

        # TODO: Try to do this in memory
        AUDIO_FILE = create_temp_filename('tmp_audio.mp3')
        REVERSED_AUDIO_FILE = create_temp_filename('tmp_reversed_audio.mp3')
        video.audio.write_audiofile(AUDIO_FILE, fps = 44100)
        AudioSegment.from_mp3(AUDIO_FILE).reverse().export(REVERSED_AUDIO_FILE)
        reversed_audio = AudioFileClip(REVERSED_AUDIO_FILE)

        return ImageSequenceClip(reversed_frames_array, fps = video.fps).set_audio(reversed_audio)