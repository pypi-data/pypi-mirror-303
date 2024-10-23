from yta_general_utils.file.checker import is_file


def delete_file(filename: str):
    """
    Deletes the provided 'filename' if existing.

    # TODO: Maybe can be using other method that generally
    # delete files (?) Please, do if possible
    """
    if not filename or not is_file(filename):
        return None
    
    from os import remove as os_remove

    os_remove(filename)