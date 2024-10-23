from yta_general_utils.audio.converter import mp3_to_wav
from yta_general_utils.file.remover import delete_file
from df.enhance import enhance, init_df, load_audio, save_audio


# TODO: Maybe this is not the best place to put this module but
# here it is. Fell free to move it.
def remove_noise_from_audio_file(audio_filename: str, audio_output_filename: str):
    """
    Removes the noise from the provided 'audio_filename' and creates a new
    file 'audio_output_filename' without noise.

    # TODO: This fails when .mp3 is used, so we need to transform into wav.

    # TODO: Output file must be also wav

    # TODO: What about audioclip instead of audiofile? Is it possible? (?)
    """
    # Based on this (https://medium.com/@devesh_kumar/how-to-remove-noise-from-audio-in-less-than-10-seconds-8a1b31a5143a)
    # https://github.com/Rikorose/DeepFilterNet
    # TODO: This is failing now saying 'File contains data in an unknon format'...
    # I don't know if maybe some library, sh*t...
    # Load default model
    TMP_WAV_FILENAME = 'tmp_wav.wav'
    if audio_filename.endswith('.mp3'):
        # TODO: Maybe it is .wav but not that format...
        mp3_to_wav(audio_filename, TMP_WAV_FILENAME)
        audio_filename = TMP_WAV_FILENAME

    model, df_state, _ = init_df()
    audio, _ = load_audio(audio_filename, sr = df_state.sr())
    # Remove the noise
    enhanced = enhance(model, df_state, audio)

    save_audio(audio_output_filename, enhanced, df_state.sr())

    try:
        delete_file(TMP_WAV_FILENAME)
    except:
        pass