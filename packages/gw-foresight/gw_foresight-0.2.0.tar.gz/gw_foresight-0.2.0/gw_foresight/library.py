import ctypes as ct
import os
from . import utils


class Library:
    """ Load a Foresight library. """

    def __init__(self, library_path: str):
        self.library_path = library_path

    def load_library(self, library_path: str):
        """
        Loads a library at the specified path and returns the loaded library.

        Parameters:
        - library_path (str): The path to the library file.

        Raises:
        - FileNotFoundError: If the specified library_path does not exist.

        Returns:
        - A CDLL object representing the loaded library.

        """
        if not os.path.isfile(library_path):
            if os.path.isdir(library_path):
                library_path = utils.get_library(self.__class__.__name__, library_path)
            else:
                raise FileNotFoundError(library_path)

        self.library_path = library_path

        with utils.CwdHandler(new_cwd=self.library_path):
            try:
                # Try to load library
                if os.name == 'nt':
                    ct.windll.kernel32.SetDllDirectoryW(None)

                return ct.cdll.LoadLibrary(self.library_path)

            except OSError as _:
                # If library fails to load and there are missing dependencies, list them
                raise
