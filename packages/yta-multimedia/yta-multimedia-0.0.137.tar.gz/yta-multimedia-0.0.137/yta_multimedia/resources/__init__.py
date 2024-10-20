from yta_general_utils.downloader.google_drive import download_file_from_google_drive
from yta_general_utils.programming.path import get_project_abspath
from yta_general_utils.file.checker import file_exists
from yta_general_utils.temp import create_temp_filename
from yta_general_utils.path import create_file_abspath


def get_resource(google_drive_url: str, output_filename: str = None):
    """
    This method has been built to be used internally to obtain
    the resources this software needs. This method will look
    for the 'output_filename' if provided, and if it exist
    locally stored, it will return that filename. If it doesn't
    exist or the 'output_filename' is not provided, it will 
    download the resource from the given 'google_drive_url',
    store it locally and return it.

    The first time a resource is downloaded from the given
    'google_drive_url', if 'output_filename' provided, will
    be stored locally with that filename. Next time, as it 
    will be found locally, it will be returned and we will
    have not to wait for the download.

    This method has been created to optimize the resource
    getting process.

    @param
        **google_drive_url**
        The Google Drive url in which we can found (and
        download) the resource.

    @param
        **output_filename**
        The filename of the resource we want to get, that
        must be a relative path from the current project
        abspath.
    """
    if not google_drive_url:
        return None
    
    output_abspath = create_temp_filename('tmp_resource.mp3')
    
    if output_filename:
        # We try to find it and return or we create the folder if doesn't exist
        output_abspath = get_project_abspath() + output_filename

        if file_exists(output_abspath):
            return output_abspath
        
        # We force to create all folders
        create_file_abspath(output_abspath)
    
    # We download the file and store it locally
    return download_file_from_google_drive(google_drive_url, output_abspath)