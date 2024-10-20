from yta_general_utils.file.checker import file_is_video_file
from yta_general_utils.checker.type import variable_is_type
from yta_general_utils.temp import create_custom_temp_filename
from yta_multimedia.image.greenscreen import remove_greenscreen_from_image
from subprocess import run
from typing import Union
from moviepy.editor import VideoFileClip


def remove_greenscreen_from_video(video_input: Union[VideoFileClip, str], output_filename: str):
    """
    Removes the green screen from the 'video_input' video so
    you get a final 'output_filename' video with transparent
    layer.
    """
    if not video_input:
        return None
    
    if not output_filename:
        return None
    
    if variable_is_type(video_input, str):
        if not file_is_video_file(video_input):
            return None
        
        video_input = VideoFileClip(video_input)

    # Export all frames
    original_frames_array = []
    for frame in video_input.iter_frames():
        frame_name = create_custom_temp_filename('tmp_frame_' + str(len(original_frames_array)) + '.png')
        original_frames_array.append(frame_name)
    video_input.write_images_sequence(create_custom_temp_filename('tmp_frame_%01d.png'), logger = 'bar')

    # Remove green screen of each frame and store it
    processed_frames_array = []
    for index, frame in enumerate(original_frames_array):
        tmp_frame_filename = create_custom_temp_filename('tmp_frame_processed_' + str(index) + '.png')
        processed_frames_array.append(tmp_frame_filename)
        remove_greenscreen_from_image(frame, tmp_frame_filename)

    # Rebuild the video
        
    # https://stackoverflow.com/a/77608713
    #ImageSequenceClip(processed_frames_array, fps = clip.fps).set_audio(clip.audio).write_videofile(output_filename, codec = 'hap_alpha', ffmpeg_params = ['-c:v', 'hap', '-format', 'hap_alpha', '-vf', 'chromakey=black:0.1:0.1'])
    # https://superuser.com/questions/1779201/combine-pngs-images-with-transparency-into-a-video-and-merge-it-on-a-static-imag
    # ffmpeg -y -i src/tmp/%d.png -c:v libx264 -vf fps=25 -pix_fmt yuva420p land.mov
    
    #clip = ImageSequenceClip(processed_frames_array, fps = clip.fps).set_audio(clip.audio).write_videofile(output_filename, codec = 'libx264', audio_codec = 'aac', temp_audiofile = 'temp-audio.m4a', remove_temp = True)
    parameters = ['ffmpeg', '-y', '-i', create_custom_temp_filename('tmp_frame_processed_%01d.png'), '-r', '30', '-pix_fmt', 'yuva420p', output_filename]

    run(parameters)

    return output_filename