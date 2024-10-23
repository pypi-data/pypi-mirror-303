from yta_general_utils.temp import create_temp_filename
from yta_general_utils.file.filename import get_file_extension, replace_file_extension
from pydub import AudioSegment


def mp3_to_wav(mp3_filename: str, output_filename: str):
    """
    Receives an .mp3 file 'mp3_filename' and turns it into a .wav
    file stored in 'output_filename'. This method will return the
    actual 'output_filename' used to export the file as it could
    has been changed by the method.
    """
    if not mp3_filename:
        raise Exception('No "mp3_filename" provided.')
    
    # TODO: Check that 'mp3_filename' is a valid mp3 filename and
    # that the file exists
    
    if not output_filename:
        # TODO: Replace this when not exporting needed
        output_filename = create_temp_filename('tmp_wav_sound.wav')

    # TODO: Make mp3 being not only a filename
    if not get_file_extension(output_filename) == 'wav':
        output_filename = replace_file_extension(output_filename, 'wav')

    # TODO: Generalize this method to swap between formats
    sound = AudioSegment.from_mp3(mp3_filename)
    # TODO: Achieve this without exporting, please
    sound.export(output_filename, format = "wav")

    return output_filename