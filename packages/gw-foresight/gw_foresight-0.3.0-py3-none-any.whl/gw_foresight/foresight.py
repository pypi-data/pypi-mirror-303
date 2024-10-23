import os
import io
import ctypes as ct

from .library import Library
from . import log
from . import utils

from contextlib import contextmanager
from typing import Union


class GwReturnObj:
    """ An object intended mostly for internal use that has different
    attributes depending on which library and functionality utilises it, such
    as `status`, `buffer`, and `buffer_bytes`
    """

    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items()]


class Foresight(Library):
    """ A high level Python wrapper for Glasswall Foresight """

    def __init__(self, library_path: str):
        super().__init__(library_path=library_path)
        self.library = self.load_library(os.path.abspath(library_path))

        log.info(f"Library Info:\n\nLoaded Glasswall {self.fs_version()} from {self.library_path}\n")

    def fs_version(self):
        """ Returns the Foresight library version.

            Returns:
                version (str): The Foresight library version.
        """

        # API function declaration
        self.library.GwForesightVersion.restype = ct.c_char_p

        # API call
        version = self.library.GwForesightVersion()

        # Convert to Python string
        version = ct.string_at(version).decode()

        return version

    def fs_create_session(self):
        """ Open a new Foresight session.

            Returns:
                session (int): An incrementing integer representing the current session.
        """

        session = self.library.GwForesightCreateSession()

        log.debug(f"\n\tSession: {session}")

        return session

    def fs_end_session(self, session: int):
        """ Terminate the session. All resources allocated by the session will be destroyed.

        Args:
            session (int): The session to close.

        Returns:
            None
        """

        if not isinstance(session, int):
            raise TypeError(session)

        self.library.GwForesightEndSession.argtypes = [ct.c_int]

        ct_session = ct.c_int(session)

        status = self.library.GwForesightEndSession(ct_session)

        if status != 0:
            log.error(f"\n\tSession: {session}\n\tstatus: {status}")
        else:
            log.debug(f"\n\tSession: {session}\n\tstatus: {status}")

        return status

    # noinspection PyUnboundLocalVariable
    @contextmanager
    def fs_new_session(self):
        """ Context manager. Opens a new session on entry and closes the session on exit. """
        try:
            session = self.fs_create_session()
            yield session
        finally:
            self.fs_end_session(session)

    def fs_run_session(self, session):
        """ Runs the Foresight session and begins processing of a file.

        Args:
            session (int): The session to run.

        Returns:
            status (int): The status of the function call.
        """

        # API function declaration
        self.library.GwForesightRunSession.argtypes = [ct.c_int]

        # Variable initialisation
        ct_session = ct.c_int(session)

        # API call
        status = self.library.GwForesightRunSession(ct_session)

        if status != 0:
            log.error(f"\n\tSession: {session}\n\tstatus: {status}")
        else:
            log.debug(f"\n\tSession: {session}\n\tstatus: {status}")

        return status

    def fs_load_input(self, session: int, input_file: Union[str, bytes, bytearray, io.BytesIO]):

        """ Register an input file or bytes for the given session.

        Args:
            session (int): The current session.
            input_file (Union[str, bytes, bytearray, io.BytesIO]): The input file path or bytes.

        Returns:
            status (int): The result of the Foresight API call.
        """

        file_buffer = None

        if not isinstance(input_file, (str, bytes, bytearray, io.BytesIO,)):
            raise TypeError(input_file)

        if isinstance(input_file, str):
            if not os.path.isfile(input_file):
                raise FileNotFoundError(input_file)

            with open(input_file, "rb") as file:
                file_buffer = file.read()

        elif isinstance(input_file, (bytes, bytearray, io.BytesIO,)):
            file_buffer = utils.as_bytes(input_file)

        if file_buffer:
            self.library.GwForesightLoadInput.argtypes = [
                ct.c_int,
                ct.c_char_p,
                ct.c_size_t,
            ]

            # Variable initialisation
            ct_session = ct.c_int(session)
            ct_buffer = ct.c_char_p(file_buffer)
            ct_buffer_length = ct.c_size_t(len(file_buffer))

            # API call
            status = self.library.GwForesightLoadInput(
                ct_session,
                ct_buffer,
                ct_buffer_length
            )

            if status != 0:
                log.error(f"\n\tSession: {session}\n\tstatus: {status}")
                raise Exception("Input registration failure")
            else:
                log.debug(f"\n\tSession: {session}\n\tstatus: {status}")
        else:
            raise Exception("Input registration failure")

        return status

    def fs_load_model(self, session: int, model: Union[str, bytes, bytearray, io.BytesIO]):
        """ Register an onnx model file or bytes for the given session.

        Args:
            session (int): The current session.
            model (Union[str, bytes, bytearray, io.BytesIO]): The onnx ml model as file path or bytes.

        Returns:
            status (int): The result of the Foresight API call.
        """

        file_buffer = None

        if not isinstance(model, (str, bytes, bytearray, io.BytesIO,)):
            raise TypeError(model)

        if isinstance(model, str):
            if not os.path.isfile(model):
                raise FileNotFoundError(model)

            with open(model, "rb") as file:
                file_buffer = file.read()

        elif isinstance(model, (bytes, bytearray, io.BytesIO,)):
            file_buffer = utils.as_bytes(model)

        if file_buffer:
            self.library.GwForesightLoadModel.argtypes = [
                ct.c_int,
                ct.c_char_p,
                ct.c_size_t,
            ]

            # Variable initialisation
            ct_session = ct.c_int(session)
            ct_buffer = ct.c_char_p(file_buffer)
            ct_buffer_length = ct.c_size_t(len(file_buffer))

            # API call
            status = self.library.GwForesightLoadModel(
                ct_session,
                ct_buffer,
                ct_buffer_length
            )

            if status != 0:
                log.error(f"\n\tSession: {session}\n\tstatus: {status}")
                raise Exception("Model registration failure")
            else:
                log.debug(f"\n\tSession: {session}\n\tstatus: {status}")
        else:
            raise Exception("Model registration failure")

        return status

    def fs_load_models(self, session: int, model: Union[str, bytes, bytearray, io.BytesIO]):
        """ Register an onnx model pack via file path or bytes for the given session.

        Args:
            session (int): The current session.
            model (Union[str, bytes, bytearray, io.BytesIO]): The onnx ml model pack as file path or bytes.

        Returns:
            status (int): The result of the Foresight API call.
        """

        file_buffer = None

        if not isinstance(model, (str, bytes, bytearray, io.BytesIO,)):
            raise TypeError(model)

        if isinstance(model, str):
            if not os.path.isfile(model):
                raise FileNotFoundError(model)

            with open(model, "rb") as file:
                file_buffer = file.read()

        elif isinstance(model, (bytes, bytearray, io.BytesIO,)):
            file_buffer = utils.as_bytes(model)

        if file_buffer:
            self.library.GwForesightLoadModels.argtypes = [
                ct.c_int,
                ct.c_char_p,
                ct.c_size_t,
            ]

            # Variable initialisation
            ct_session = ct.c_int(session)
            ct_buffer = ct.c_char_p(file_buffer)
            ct_buffer_length = ct.c_size_t(len(file_buffer))

            # API call
            status = self.library.GwForesightLoadModels(
                ct_session,
                ct_buffer,
                ct_buffer_length
            )

            if status != 0:
                log.error(f"\n\tSession: {session}\n\tstatus: {status}")
                raise Exception("Model registration failure")
            else:
                log.debug(f"\n\tSession: {session}\n\tstatus: {status}")
        else:
            raise Exception("Model registration failure")

        return status

    def fs_load_config(self, session: int, config: Union[str, bytes, bytearray, io.BytesIO]):
        """ Register foresight config file for the given session.

        Args:
            session (int): The current session.
            config (Union[str, bytes, bytearray, io.BytesIO]): The foresight config file as file path or bytes.

        Returns:
            status (int): The result of the Foresight API call.
        """

        file_buffer = None

        if not isinstance(config, (str, bytes, bytearray, io.BytesIO,)):
            raise TypeError(config)

        if isinstance(config, str):
            if not os.path.isfile(config):
                raise FileNotFoundError(config)

            with open(config, "rb") as file:
                file_buffer = file.read()

        elif isinstance(config, (bytes, bytearray, io.BytesIO,)):
            file_buffer = utils.as_bytes(config)

        if file_buffer:
            self.library.GwForesightLoadConfig.argtypes = [
                ct.c_int,
                ct.c_char_p,
                ct.c_size_t,
            ]

            # Variable initialisation
            ct_session = ct.c_int(session)
            ct_buffer = ct.c_char_p(file_buffer)
            ct_buffer_length = ct.c_size_t(len(file_buffer))

            # API call
            status = self.library.GwForesightLoadConfig(
                ct_session,
                ct_buffer,
                ct_buffer_length
            )

            if status != 0:
                log.error(f"\n\tSession: {session}\n\tstatus: {status}")
                raise Exception("Config registration failure")
            else:
                log.debug(f"\n\tSession: {session}\n\tstatus: {status}")
        else:
            raise Exception("Config registration failure")

        return status

    def fs_set_output(self, session):
        """ Register an output file for the given session.

        Args:
            session (int): The current session.
        Returns:
            gw_return_object (glasswall.GwReturnObj): A GwReturnObj instance with the attribute 'status' indicating the
            result of the function call. If successful, output_file attributes 'buffer', and 'buffer_length' are
            included containing the file content and file size.
        """

        output_file = GwReturnObj()

        # API function declaration
        self.library.GwForesightSetOutput.argtypes = [
            ct.c_int,
            ct.POINTER(ct.c_void_p),
            ct.POINTER(ct.c_size_t)
        ]

        # Variable initialisation
        ct_session = ct.c_int(session)
        output_file.buffer = ct.c_void_p()
        output_file.buffer_length = ct.c_size_t(0)

        # API call
        output_file.status = self.library.GwForesightSetOutput(
            ct_session,
            ct.byref(output_file.buffer),
            ct.byref(output_file.buffer_length)
        )

        if output_file.status != 0:
            log.error(f"\n\tSession: {session}\n\tstatus: {output_file.status}")
            raise Exception("Output registration failure")
        else:
            log.debug(f"\n\tSession: {session}\n\tstatus: {output_file.status}")

        return output_file

    def fs_set_log_output(self, session):
        """ Register an output log file for the given session.

        Args:
            session (int): The current session.
        Returns:
            gw_return_object (glasswall.GwReturnObj): A GwReturnObj instance with the attribute 'status' indicating the
            result of the function call. If successful, log_file attributes 'buffer', and 'buffer_length' are
            included containing the log file content and size.
        """

        log_file = GwReturnObj()

        # API function declaration
        self.library.GwForesightSetLogOutput.argtypes = [
            ct.c_int,
            ct.POINTER(ct.c_void_p),
            ct.POINTER(ct.c_size_t)
        ]

        # Variable initialisation
        ct_session = ct.c_int(session)
        log_file.buffer = ct.c_void_p()
        log_file.buffer_length = ct.c_size_t(0)

        # API call
        log_file.status = self.library.GwForesightSetLogOutput(
            ct_session,
            ct.byref(log_file.buffer),
            ct.byref(log_file.buffer_length)
        )

        if log_file.status != 0:
            log.error(f"\n\tsession: {session}\n\tstatus: {log_file.status}")
            raise Exception("Output log registration failure")
        else:
            log.debug(f"\n\tsession: {session}\n\tstatus: {log_file.status}")

        return log_file

    def predict(self, input_file: Union[str, bytes, bytearray, io.BytesIO],
                onnx_model: Union[str, bytes, bytearray, io.BytesIO],
                output_file: Union[None, str] = None,
                config_file: Union[str, bytes, bytearray, io.BytesIO] = None,
                log_enabled: bool = False,
                is_pack: bool = False):
        """ Runs a foresight prediction on the provided XML file.

        Args:
            input_file (Union[str, bytes, bytearray, io.BytesIO]): The input file path or bytes.
            onnx_model (Union[str, bytes, bytearray, io.BytesIO]): The serialised mode as a file path or bytes.
            output_file (Union[None, str], optional): The output file path where the report will be written.
            config_file (Union[str, bytes, bytearray, io.BytesIO], optional): The foresight config file as a file or
            bytes.
            log_enabled (bool): Flag indicating if foresight should write out a log file.
            is_pack (bool): Denotes whether the onnx_model is a pack or single model
        Returns:
            json report (bytes): JSON report containing prediction scores.
            analysis report (bytes): original XML engine analysis report.
        """

        # Validate arg types
        if not isinstance(input_file, (str, bytes, bytearray, io.BytesIO)):
            raise TypeError(input_file)
        if not isinstance(onnx_model, (str, bytes, bytearray, io.BytesIO)):
            raise TypeError(onnx_model)
        if not isinstance(output_file, (type(None), str)):
            raise TypeError(output_file)
        if not isinstance(config_file, (type(None), str, bytes, bytearray, io.BytesIO)):
            raise TypeError(config_file)

        # Convert string path arguments to absolute paths
        if isinstance(input_file, str):
            if not os.path.isfile(input_file):
                raise FileNotFoundError(input_file)
            input_file = os.path.abspath(input_file)

        if isinstance(config_file, str):
            if not os.path.isfile(config_file):
                raise FileNotFoundError(config_file)
            config_file = os.path.abspath(config_file)

        if isinstance(onnx_model, str):
            if not os.path.isfile(onnx_model):
                raise FileNotFoundError(onnx_model)
            onnx_model = os.path.abspath(onnx_model)

        if isinstance(output_file, str):
            output_file = os.path.abspath(output_file)
            # make directories that do not exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
        # Convert memory inputs to bytes
        if isinstance(input_file, (bytes, bytearray, io.BytesIO)):
            input_file = utils.as_bytes(input_file)
        if isinstance(onnx_model, (bytes, bytearray, io.BytesIO)):
            onnx_model = utils.as_bytes(onnx_model)
        if isinstance(config_file, (bytes, bytearray, io.BytesIO)):
            config_file = utils.as_bytes(config_file)
        with utils.CwdHandler(self.library_path):
            with self.fs_new_session() as session:

                status = self.fs_load_config(session, config_file)
                if status != 0:
                    log.error(f"Unable to to load config file: {status}")
                    return None, None, None

                status = self.fs_load_input(session, input_file)
                if status != 0:
                    log.error(f"Unable to to load input file: {status}")
                    return None, None, None

                if is_pack:
                    status = self.fs_load_models(session, onnx_model)
                else:
                    status = self.fs_load_model(session, onnx_model)

                if status != 0:
                    log.error(f"Unable to to load model file(s): {status}")
                    return None, None, None

                register_output = self.fs_set_output(session)
                register_output_log = None
                if log_enabled:
                    register_output_log = self.fs_set_log_output(session)

                status = self.fs_run_session(session)

                input_file_repr = f"{type(input_file)} length {len(input_file)}" if \
                    isinstance(input_file, (bytes, bytearray,)) else input_file.__sizeof__() if \
                    isinstance(input_file, io.BytesIO) else input_file
                if status != 0:
                    log.error(
                        f"\n\tinput_file: {input_file_repr}\n\toutput_file: {output_file}\n\tsession: "
                        f"{session}\n\tstatus: {status}")
                    file_bytes = None
                else:
                    log.debug(
                        f"\n\tinput_file: {input_file_repr}\n\toutput_file: {output_file}\n\tsession: "
                        f"{session}\n\tstatus: {status}")

                    file_bytes = utils.buffer_to_bytes(
                        register_output.buffer,
                        register_output.buffer_length
                    )

                log_file_bytes = None
                if log_enabled:
                    log_file_bytes = utils.buffer_to_bytes(
                        register_output_log.buffer,
                        register_output_log.buffer_length
                    )
                    if isinstance(output_file, str):
                        if log_file_bytes:
                            with open(output_file + ".log", "wb") as logfile:
                                # Write content to the file
                                logfile.write(log_file_bytes)

                if isinstance(output_file, str) and file_bytes:
                    with open(output_file, "wb") as file:
                        # Write content to the file
                        file.write(file_bytes)

                # Ensure memory allocated is not garbage collected
                # noinspection PyStatementEffect
                register_output

                return file_bytes, input_file, log_file_bytes
