"""
    # TODO: Refactor all possible methods below to make them dynamic
    # and return the content if no 'output_filename' provided.
"""
from yta_general_utils.file.writer import write_binary_file
from typing import Union

import requests


def get_file(url: str, output_filename: Union[str, None] = None):
    """
    This method sends a request to the provided 'url'
    if provided and obtains the file content (if 
    possible). It will write the obtained file locally
    as 'output_filename' if provided.

    This method returns the file content data as 
    obtained from the requested (.content field).
    """
    if not url:
        raise Exception('No "url" provided.')
    
    content = requests.get(url).content

    if output_filename:
        write_binary_file(content, output_filename)

    return content

def download_file(url: str, output_filename: str):
    """
    Receives a downloadable url as 'url' and downloads that file in
    our system as 'output_filename'.
    """
    if not output_filename:
        raise Exception('No "output_filename" provided to save the file.')

    return get_file(url, output_filename)