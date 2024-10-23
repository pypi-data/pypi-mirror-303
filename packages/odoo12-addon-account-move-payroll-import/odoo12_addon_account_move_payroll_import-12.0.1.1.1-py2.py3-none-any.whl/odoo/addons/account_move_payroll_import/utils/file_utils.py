import os
import base64


EXTENSIONS = [".csv", ".xls", ".xlsx"]


def get_file_extension(file_name):
    """
    Get the file extension from the file name.
    """
    if file_name:
        return os.path.splitext(file_name)[-1]
    return False


def decode_file(file_contents):
    """
    Decode the file content.
    """
    return base64.b64decode(file_contents)


def is_valid_extension(file_name):
    """
    Get the valid file extension.
    """
    ext = get_file_extension(file_name)
    if ext not in EXTENSIONS:
        return False
    return ext[1:]
