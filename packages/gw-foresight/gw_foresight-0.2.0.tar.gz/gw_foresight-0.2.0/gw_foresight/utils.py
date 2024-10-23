import ctypes as ct
import io
import os
import pathlib
import tempfile
from typing import Union


def as_bytes(file_: Union[bytes, bytearray, io.BytesIO]):
    """ Returns file_ as bytes.

    Args:
        file_ (Union[bytes, bytearray, io.BytesIO]): The file

    Returns:
        bytes

    Raises:
        TypeError: If file_ is not an instance of: bytes, bytearray, io.BytesIO
    """
    if isinstance(file_, bytes):
        return file_
    elif isinstance(file_, bytearray):
        return bytes(file_)
    elif isinstance(file_, io.BytesIO):
        return file_.read()
    else:
        raise TypeError(file_)


def buffer_to_bytes(buffer: ct.c_void_p, buffer_length: ct.c_size_t):
    """ Convert ctypes buffer and buffer_length to bytes.

    Args:
        buffer (ct.c_void_p()): The file buffer.
        buffer_length (ct.c_size_t()): The file buffer length.

    Returns:
        bytes (bytes): The file as bytes.
    """

    file_buffer = (ct.c_byte * buffer_length.value)()
    ct.memmove(file_buffer, buffer.value, buffer_length.value)

    return bytes(file_buffer)


class CwdHandler:
    """ Changes the current working directory to new_cwd on __enter__, and back to previous cwd on __exit__.

    Args:
        new_cwd (str): The new current working directory to temporarily change to.
    """

    def __init__(self, new_cwd: str):
        self.new_cwd = new_cwd if os.path.isdir(new_cwd) else os.path.dirname(new_cwd)
        self.old_cwd = os.getcwd()

    def __enter__(self):
        os.chdir(self.new_cwd)

    def __exit__(self, _type, value, traceback):
        os.chdir(self.old_cwd)


# noinspection PyIncorrectDocstring
def get_library(library: str, directory: str):
    """ Returns a path to the specified library found from the current directory or any subdirectory.
    If multiple libraries exist, returns the file with the latest modified time.

    Args:
        library (str): TBD
        directory (str): TBD
    Returns:
        TBD

    Raises:
        TBD
    """

    # TODO: Implement to provide ability to search for relevant libraries.
    #  This will allow for debug & release libs to be loaded, as well as providing option to specify
    #  a directory or file path

    return ""


# noinspection PyBroadException
def load_dependencies(dependencies: list, ignore_errors: bool = False):
    """ Calls ctypes.cdll.LoadLibrary on each file path in `dependencies`.

    Args:
        dependencies (list): A list of absolute file paths of library dependencies.
        ignore_errors (bool, optional): Default False, avoid raising exceptions from ct.cdll.LoadLibrary if
        ignore_errors is True.

    Returns:
        missing_dependencies (list): A list of missing dependencies, or an empty list.
    """
    missing_dependencies = [dependency for dependency in dependencies if not os.path.isfile(dependency)]

    for dependency in dependencies:
        # Try to load dependencies that exist
        if dependency not in missing_dependencies:
            try:
                ct.cdll.LoadLibrary(dependency)
            except Exception:
                if ignore_errors:
                    pass
                else:
                    raise

    return missing_dependencies


class TempFilePath:
    """ Gives a path to a uniquely named temporary file that does not currently exist on __enter__, deletes the file if
    it exists on __exit__.

    Args:
        directory (Union[str, None], optional): The directory to create a temporary file in.
        delete (bool, optional): Default True. Delete the temporary file on __exit__
    """

    def __init__(self, directory: Union[str, None] = None, delete: bool = True):
        # Validate args
        if not isinstance(directory, (str, type(None))):
            raise TypeError(directory)
        if isinstance(directory, str) and not os.path.isdir(directory):
            raise NotADirectoryError(directory)
        if not isinstance(delete, bool):
            raise TypeError(delete)

        self.temp_file = None
        self.directory = directory or tempfile.gettempdir()
        self.delete = delete

        while self.temp_file is None or os.path.isfile(self.temp_file):
            # noinspection PyProtectedMember,PyUnresolvedReferences
            self.temp_file = os.path.join(self.directory, next(tempfile._get_candidate_names()))

        # Normalize
        self.temp_file = str(pathlib.Path(self.temp_file).resolve())

        # Create temp directory if it does not exist
        os.makedirs(os.path.dirname(self.temp_file), exist_ok=True)

    def __enter__(self):
        return self.temp_file

    def __exit__(self, _type, value, traceback):
        if self.delete:
            if os.path.isfile(self.temp_file):
                os.remove(self.temp_file)
