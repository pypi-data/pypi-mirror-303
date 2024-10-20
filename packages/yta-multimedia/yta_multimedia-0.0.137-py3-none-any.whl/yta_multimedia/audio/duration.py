from yta_general_utils.file import rename_file
from yta_general_utils.file.checker import file_is_audio_file
from yta_general_utils.temp import create_temp_filename
from moviepy.editor import AudioFileClip


def crop_audio_file(audio_filename: str, duration: float, output_filename: str):
    """
    Crops the 'audio_filename' provided to the requested 'duration'.

    This method returns the new audio 'output_filename' if valid, or
    False if it was not possible to crop it.
    """
    if not audio_filename:
        return None
    
    if not output_filename:
        return None

    from moviepy.editor import AudioFileClip

    audio_clip = AudioFileClip(audio_filename)

    if audio_clip.duration < duration:
        # TODO: Exception, None, review this
        print('audio is shorter than requested duration')
        return False
    
    audio_clip.set_duration(duration).write_audiofile(output_filename)

    return output_filename

def speedup_audio_file(audio_filename: str, new_duration: int, output_filename: str):
    """
    Receives an audio 'audio_filename' and makes it have the provided
    'new_duration' if shorter than the real one. It will speed up the
    audio to fit that new duration and will store the new audio file
    as 'output_filename'.
    """
    if not audio_filename:
        return None
    
    if not file_is_audio_file(audio_filename):
        return None
    
    audio = AudioFileClip(audio_filename)
    if audio.duration <= new_duration:
        return None
    
    if not output_filename:
        return None

    from pydub import AudioSegment
    from pydub.effects import speedup

    # We calculate audio the speed_up factor 
    speed_factor = audio.duration / new_duration

    # We use a tmp file because input filename could be same as output 
    # TODO: Careful with extension
    tmp_audio_filename = create_temp_filename('tmp_audio_shortened.wav')
    # TODO: What about format?
    sound = AudioSegment.from_file(audio_filename, format = "mp3")
    final = speedup(sound, playback_speed = speed_factor)
    final.export(tmp_audio_filename, format = "mp3")
    # TODO: This is giving 'PermissionError [WindError 5]' when input 
    # and output are the same
    rename_file(tmp_audio_filename, output_filename, True)
