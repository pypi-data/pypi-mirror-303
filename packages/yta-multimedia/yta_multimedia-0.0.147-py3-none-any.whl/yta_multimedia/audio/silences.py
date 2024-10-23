from pydub import AudioSegment, silence

# TODO: Maybe rename to 'silence.py' in singular (?)
def detect_silences_in_audio_file(audio_filename: str, silence_ms_min_length: int = 250):
    """
    This method detects the silences existing in the provided 'audio_filename' that
    are at least 'silence_ms_min_length' long (this time is in milliseconsd). It 
    will return an array containing tuples (X.XX, Y.YY) of start and end silence 
    moments (in seconds).
    """
    # TODO: Getting AudioSegment from AudioFileClip and not files would be awesome
    audio = __get_audio_segment(audio_filename)

    dBFS = audio.dBFS
    silences = silence.detect_silence(audio, min_silence_len = silence_ms_min_length, silence_thresh = dBFS - 16)

    # [(1.531, 1.946), (..., ...), ...] in seconds
    return [((start / 1000), (stop / 1000)) for start, stop in silences]

# TODO: These below should not be here maybe (?)
# About sound intensity
def test_sound_intensity(audio_filename):
    audio: AudioSegment = __get_audio_segment(audio_filename)
    # TODO: Do more stuff 

def __get_audio_segment(audio_filename: str) -> AudioSegment:
    """
    Reads the provided 'audio_filename' and returns it as a
    'pydub' library AudioSegment object.
    """
    from yta_general_utils.file_processor import file_is_audio_file, get_file_extension
    
    if not audio_filename:
        return None
    
    if not file_is_audio_file(audio_filename):
        return None
    
    
    myaudio = AudioSegment.from_file(audio_filename)

    """
    # TODO: This is really needed? I need to do more tests
    extension = get_file_extension(audio_filename)
    if extension == 'mp3':
        myaudio = AudioSegment.from_mp3(audio_filename)
    elif extension == 'wav':
        myaudio = AudioSegment.from_wav(audio_filename)
    else:
        # TODO: Do this work? I think no, because it is not configured
        myaudio = AudioSegment.from_file(audio_filename)
    """

    return myaudio


