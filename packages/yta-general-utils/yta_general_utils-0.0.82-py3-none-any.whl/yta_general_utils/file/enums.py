from enum import Enum


class FileSearchOption(Enum):
    """
    Enum that allows us setting the strategy dynamically when 
    searching for files.
    """
    FILES_AND_FOLDERS = 'fifo'
    """
    This option, when set, will return files and folders.
    """
    FILES_ONLY = 'fi'
    """
    This option, when set, will return files only.
    """
    FOLDERS_ONLY = 'fo'
    """
    This option, when set, will return folders only.
    """

class FileType(Enum):
    """
    Enum that represents the different file types and the valid
    extensions we accept for those file types. This Enum is to
    be used when checking filenames parameter.

    For example, we will use this to make sure the filename they
    gave to us is a video file type if we are storing a video 
    file.
    """
    IMAGE = ['.png', '.jpeg', '.jpg', '.webp', '.bmp']
    AUDIO = ['.wav', '.mp3', '.m4a'] # TODO: Add more types
    VIDEO = ['.mov', '.mp4', '.webm', '.avi'] # TODO: Add more types