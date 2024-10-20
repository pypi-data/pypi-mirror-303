from yta_general_utils.file.checker import file_is_audio_file
from yta_general_utils.temp import create_temp_filename
from moviepy.editor import AudioFileClip, CompositeAudioClip
from pydub import AudioSegment
from typing import Union

import numpy as np
import io
import scipy.io.wavfile as wavfile


# TODO: Refactor this, please
def append_audio_clip_to_audio_clip(base_audio_clip: AudioFileClip, new_audio_clip: AudioFileClip, start_time: float = 0.0, output_filename: str = None):
    """
    We receive a 'base_audio_clip' in which we will append the 'new_audio_clip'
    starting at 'start_time' seconds since the first one started. A combined 
    audio will be generated and returned.

    If 'output_filename' is provided, it will be also written in that 
    destination.
    """
    if start_time < 0:
        start_time = 0

    combined = CompositeAudioClip([base_audio_clip, new_audio_clip.set_start(start_time)])
    # TODO: Why 441000 here below?
    combined.fps = 44100

    if output_filename:
        combined.write_audiofile(output_filename)

    return combined

# TODO: Refactor this, please
def append_audio_file_to_audio_file(base_audio_filename: str, new_audio_filename: str, start_time: float = 1.0, output_filename: str = None):
    """
    We receive an audio file called 'base_audio_filename' and we append the provided
    'new_audio_filename' to that existing audio to sound over it. That second 
    sound will start in the 'start_time' second of the first 'audio_filename'.

    If 'output_filename' provided, it will write the new combined audio. If not,
    it will only return the new CompositeAudioClip object.

    # TODO: Is this method really necessary (?) I think it is not...
    """
    if not base_audio_filename:
        return None
    
    if not file_is_audio_file(base_audio_filename):
        return None
    
    if not new_audio_filename:
        return None
    
    if not file_is_audio_file(new_audio_filename):
        return None
    
    if start_time < 0:
        return None

    return append_audio_clip_to_audio_clip(AudioFileClip(base_audio_filename), AudioFileClip(new_audio_filename), start_time, output_filename)


def audio_to_audiosegment(audio):
    """
    Forces the provided 'audio' to be a pydub AudioSegment
    and returns it if valid 'audio' provided or raises an
    Exception if not.
    """
    if not audio:
        raise Exception('No "audio" provided.')
    
    if isinstance(audio, str):
        if not file_is_audio_file(audio):
            raise Exception('Provided "audio" filename is not a valid audio file.')
        audio = AudioSegment.from_file(audio)
    elif isinstance(audio, np.ndarray):
        # TODO: Check this
        audio = numpy_to_audiosegment(audio)
    elif isinstance(audio, AudioFileClip):
        audio = audiofileclip_to_audiosegment(audio)
    elif isinstance(audio, CompositeAudioClip):
        audio = compositeaudioclip_to_audiosegment(audio)

    return audio

def audio_to_audiofileclip(audio):
    """
    Forces the provided 'audio' to be a moviepy AudioFileClip
    and returns it if valid 'audio' provided or raises an
    Exception if not.
    """
    if not audio:
        raise Exception('No "audio" provided.')
    
    if isinstance(audio, str):
        if not file_is_audio_file(audio):
            raise Exception('Provided "audio" filename is not a valid audio file.')
        audio = AudioFileClip(audio)
    elif isinstance(audio, np.ndarray):
        # TODO: Check this works
        audio = numpy_to_audiofileclip(audio)
    elif isinstance(audio, AudioSegment):
        audio = audiosegment_to_audiofileclip(audio)

    return audio

def audiosegment_to_audiofileclip(audio: AudioSegment):
    """
    This method reads the provided AudioSegment as a buffer and converts
    it to a moviepy AudioFileClip without writting any file.

    TODO: Please, make it through memory and not writting files.
    """
    if not audio:
        raise Exception('No "audio" provided.')
    
    if not isinstance(audio, AudioSegment):
        raise Exception('The "audio" parameter provided is not an AudioSegment.')
    
    # TODO: I have not been able to create an AudioFileClip dinamically
    # from memory information. I don't want to write but...
    tmp_filename = create_temp_filename('tmp_audio.wav')
    audio.export(tmp_filename, format = 'wav')

    return AudioFileClip(tmp_filename)

def audiofileclip_to_audiosegment(audio: AudioFileClip):
    """
    This method returns the provided 'audio' moviepy AudioFileClip converted
    to a pydub AudioSegment.

    TODO: This method currently writes a temporary file to make the 
    conversion. This needs to be improved to avoid writting files.
    """
    if not audio:
        raise Exception('No "audio" provided.')
    
    if not isinstance(audio, AudioFileClip):
        raise Exception('The "audio" parameter provided is not an AudioFileClip.')

    # TODO: Please, improve this to be not writting files
    tmp_filename = create_temp_filename('tmp_audio.wav')
    audio.write_audiofile(tmp_filename)
    audio = AudioSegment.from_file(tmp_filename, format = 'wav')

    return audio

def compositeaudioclip_to_audiosegment(audio: CompositeAudioClip):
    """
    This method returns the provided 'audio' moviepy CompositeAudioClip
    converted to a pydub AudioSegment.

    TODO: This method currently writes a temporary file to make the 
    conversion. This needs to be improved to avoid writting files.
    """
    if not audio:
        raise Exception('No "audio" provided.')
    
    if not isinstance(audio, CompositeAudioClip):
        raise Exception('The "audio" parameter provided is not an CompositeAudioClip.')
    
    # TODO: Please, improve this to be not writting files
    tmp_filename = create_temp_filename('tmp_audio.wav')
    audio.write_audiofile(tmp_filename)
    audio = AudioSegment.from_file(tmp_filename, format = 'wav')

    return audio

# TODO: This has not been tested properly
def numpy_to_audiosegment(audio, sample_rate):
    """
    Convers the provided 'audio' numpy array, that contains the audio data
    and must be in float32 or int16, to a pydub AudioSegment.
    """
    # Normalize audio_array if it's not already in int16 format
    if audio.dtype != np.int16:
        if audio.dtype != np.float32:
            raise Exception('The "audio" parameter provided is not np.int16 nor np.float32.')
        
        # Assuming the audio_array is in float32 with values between -1 and 1
        audio = (audio * 32767).astype(np.int16)
    
    # Create a BytesIO object
    with io.BytesIO() as buffer:
        wavfile.write(buffer, sample_rate, audio)
        buffer.seek(0)
        
        audio_segment = AudioSegment.from_file(buffer, format = 'wav')
    
    return audio_segment

# TODO: This method has not been tested properly.
def audiosegment_to_numpy(audio: AudioSegment):
    """
    This method turns the provided 'audio' AudioSegment into a numpy
    array by converting it first to an AudioFileClip and then to a
    numpy.

    TODO: Please, maybe it is a better (more direct) way

    TODO: This method has not been tested properly
    """
    if not audio:
        raise Exception('No "audio" provided.')
    
    if not isinstance(audio, AudioSegment):
        raise Exception('The "audio" parameter provided is not an AudioSegment.')
    
    # TODO: Maybe this is not the best way, I need to test and improve this
    return np.array(audio.get_array_of_samples())
    #return audiofileclip_to_numpy(audiosegment_to_audiofileclip(audio))


# TODO: This has not been tested properly
def audiofileclip_to_numpy(audio: Union[AudioFileClip]):
    """
    Convers the provided 'audio' moviepy AudioFileClip to a numpy
    array that will be np.float32.
    """
    if not audio:
        raise Exception('No "audio" provided.')
    
    if not isinstance(audio, AudioFileClip):
        raise Exception('The "audio" parameter provided is not a moviepy AudioFileClip.')

    chunk_size = 5*1024*1024
    audio_chunks = []
    for chunk in audio.iter_chunks(chunksize = chunk_size):
        # Convertir cada fragmento a un array numpy y añadirlo a la lista
        audio_array = np.frombuffer(chunk, dtype=np.int16)
        
        # Normalizar si el audio es estéreo (tendría dos columnas)
        if len(audio_array) > 0 and len(audio_array) % 2 == 0:
            audio_array = audio_array.reshape(-1, 2)
        
        audio_chunks.append(audio_array)
    
    # Concatenar todos los fragmentos en un solo array
    full_audio_array = np.concatenate(audio_chunks, axis = 0)
    
    # Convertir a float32 y normalizar
    full_audio_array = full_audio_array.astype(np.float32)
    if np.max(np.abs(full_audio_array)) > 1.0:
        full_audio_array /= np.max(np.abs(full_audio_array))
    
    return full_audio_array

# TODO: This has not been tested properly
def numpy_to_audiofileclip(audio: np.ndarray):
    if not audio:
        raise Exception('No "audio" provided.')
    
    if not isinstance(audio, np.ndarray):
        # TODO: Check this works
        raise Exception('The "audio parameter provided is not a np.ndarray.')
    
    # TODO: This won't work
    AudioFileClip(audio)