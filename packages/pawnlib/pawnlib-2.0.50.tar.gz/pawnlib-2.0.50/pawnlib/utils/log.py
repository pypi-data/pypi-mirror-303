#!/usr/bin/env python3
import os
import logging
import sys
from logging import handlers
import traceback
import datetime
from pawnlib.config.globalconfig import pawnlib_config, pawn, Null
from rich.console import Console
from rich.logging import RichHandler
from rich.text import Text
from typing import Callable
import re
import inspect

try:
    from typing import Literal, Union
except ImportError:
    from typing_extensions import Literal, Union


# class ConsoleLoggerAdapter:
#     def __init__(self, logger: Union[logging.Logger, Console, Null], logger_name="", verbose: bool = False):
#         """
#         Wrapper class to unify logging methods for logging.Logger and rich.Console.
#
#         :param logger: The logger object (logging.Logger or rich.Console)
#         :param verbose: If True, set logging to DEBUG level.
#         """
#         self.verbose = verbose
#         if isinstance(logger, ConsoleLoggerAdapter):
#             self.logger = logger.logger
#         else:
#             self.logger = logger
#
#         if self.logger is None:
#             self.logger = self._create_default_logger(logger_name)
#         elif isinstance(self.logger, Null):
#             self.logger = pawn.console
#             pawn.console.log("[red][ERROR][/red] Logger instance is Null. Using default logger.")
#
#         if isinstance(self.logger, logging.Logger):
#             self.logger.setLevel(logging.DEBUG if self.verbose else logging.INFO)
#
#     def _create_default_logger(self, logger_name="") -> logging.Logger:
#         """
#         Create a default logger for the WebSocket client if none is provided.
#         """
#         logger = logging.getLogger(logger_name)
#         logger.propagate = False
#         if not logger.handlers:
#             handler = logging.StreamHandler()
#             formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
#             handler.setFormatter(formatter)
#             logger.addHandler(handler)
#             logger.setLevel(logging.DEBUG if self.verbose > 0 else logging.INFO)
#         return logger
#
#     def _escape_all_brackets(self, message: str) -> str:
#         """
#         Escape all square brackets in the message.
#         :param message: The log message.
#         :return: The message with all square brackets escaped.
#         """
#         # Escape all [ and ] in the message
#         message = message.replace("[", r"\[")
#         return message
#
#     def _escape_non_tag_brackets(self, message: str) -> str:
#         """
#         Escape non-rich-tag '[' in the message without altering rich tags.
#
#         :param message: The log message.
#         :return: The message with non-rich-tag '[' escaped.
#         """
#         import re
#
#         VALID_RICH_TAGS = {
#             'red', 'bold', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white', 'black',
#             'italic', 'underline', 'blink', 'reverse', 'strike', 'dim',
#             'blink2', 'conceal', 'crossed_out', 'default', 'frame', 'framed',
#             'overline', 'encircle', 'shadow', 'outline', 'hidden', 'standout',
#             'superscript', 'subscript', 'link', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
#             # Add more valid tags as needed
#         }
#
#         result = ''
#         i = 0
#         length = len(message)
#
#         while i < length:
#             if message[i] == '[':
#                 # Possible start of a tag
#                 tag_match = re.match(r'\[/?([a-zA-Z0-9 _-]+)\]', message[i:])
#                 if tag_match:
#                     tag_content = tag_match.group(1)
#                     # Check if all parts of the tag are valid
#                     tag_parts = tag_content.split()
#                     if all(part in VALID_RICH_TAGS for part in tag_parts):
#                         # It's a valid rich tag, copy it as is
#                         tag_text = tag_match.group(0)
#                         result += tag_text
#                         i += len(tag_text)
#                     else:
#                         # Not a valid rich tag, escape the '['
#                         result += r'\['
#                         i += 1
#                 else:
#                     # Not a tag, escape the '['
#                     result += r'\['
#                     i += 1
#             else:
#                 result += message[i]
#                 i += 1
#
#         return result
#
#
#     def _log(self, message: str, level: str = "info"):
#         """
#         Internal method to handle logging for both Logger and Console.
#         """
#         level = level.lower()
#         stack_offset = self._get_stack_offset()
#
#         if isinstance(self.logger, logging.Logger):
#             getattr(self.logger, level, self.logger.info)(message, stacklevel=stack_offset)
#         elif isinstance(self.logger, Console):
#         # elif isinstance(self.logger, Console) :
#             message = self._escape_non_tag_brackets(message)  # Escape brackets in the message
#
#             if level == "debug":
#                 self.logger.debug(message, _stack_offset=4)
#             else:
#                 level_tags = {
#                     "info": "[cyan]INFO   [/cyan]",
#                     "error": "[red]ERROR  [/red]",
#                     "warn": "[yellow]WARN   [/yellow]",
#                     "critical": "[bold red]CRITICAL[/bold red]",
#                 }
#                 tag = level_tags.get(level, "[cyan]INFO   [/cyan]")
#                 self.logger.log(f"{tag} {message}", _stack_offset=stack_offset)
#         else:
#             pass
#
#     def _get_stack_offset(self) -> int:
#         # 현재 함수가 호출된 스택 깊이
#         # current_frame = inspect.currentframe()
#         # _get_stack_offset() -> _log() -> logging 메서드 순으로 호출되므로, 3을 반환
#         return 3
#
#     # Public methods for common logging levels
#     def info(self, message: str):
#         self._log(message, "info")
#
#     def error(self, message: str):
#         self._log(message, "error")
#
#     def warn(self, message: str):
#         self._log(message, "warn")
#
#     def debug(self, message: str):
#         self._log(message, "debug")
#
#     def critical(self, message: str):
#         self._log(message, "critical")
#
#     def __repr__(self):
#         """
#         Return a string representation of the ConsoleLoggerAdapter showing the type of logger used.
#         """
#         logger_type = self._get_logger_type(self.logger)
#         return f"<ConsoleLoggerAdapter logger_type={logger_type}>"
#
#     def _get_logger_type(self, logger):
#         """
#         Helper method to recursively determine the type of the logger.
#         """
#         if isinstance(logger, ConsoleLoggerAdapter):
#             return self._get_logger_type(logger.logger)
#         elif isinstance(logger, logging.Logger):
#             return "Logger"
#         elif isinstance(logger, Console):
#             return "Console"
#         elif isinstance(logger, Null):
#             return "Null"
#         else:
#             return type(logger).__name__


class CustomLog:
    """CustomLog

    :param name: logger name

    Example:

        .. code-block:: python

            from pawnlib.utils.log import CustomLog

            file_name = './time_log.txt'
            logger = CustomLog("custom_log")
            logger.set_level('DEBUG')
            logger.stream_handler("INFO")
            logger.time_rotate_handler(filename=file_name,
                                       when="M",
                                       interval=2,
                                       backup_count=3,
                                       level="INFO"
                                       )
            idx = 1
            logger.log.debug(logger.log_formatter(f'debug {idx}'))
            logger.log.info(logger.log_formatter(f'info {idx}'))
            logger.log.warning(logger.log_formatter(f'warning {idx}'))
            logger.log.error(logger.log_formatter(f'error {idx}'))
            logger.log.critical(logger.log_formatter(f'critical {idx}'))

    """

    def __init__(self, name):
        self.log = logging.getLogger(name)
        self.log.propagate = True
        # self.formatter = logging.Formatter("%(levelname).1s|%(asctime)s.%(msecs)06d|-|%(name)s|%(message)s", "%Y%m%d-%H:%M:%S")
        # self.formatter = logging.Formatter(f"%(levelname).1s|%(asctime)s.%(msecs)06d|-|%(name)s|%(filename)s:%(lineno)d %(funcName)-15s| %(message)s", "%Y%m%d-%H:%M:%S")
        self.formatter = logging.Formatter(
            f"%(levelname).1s|%(asctime)s.%(msecs)06d|-|%(name)s|%(filename)s:%(lineno)d| %(message)s",
            "%Y%m%d-%H:%M:%S"
        )
        self.levels = {
            "DEBUG": logging.DEBUG,
            "INFO": logging.INFO,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL
        }

    def set_level(self, level):
        self.log.setLevel(self.levels[level])

    def log_formatter(self, msg):
        """

        :param msg:
        :return:
        """
        log_str = f"{msg}"
        return log_str

    def stream_handler(self, level):
        """
        :param level:

        Note:
            level

            * "DEBUG" : logging.DEBUG ,
            * "INFO" : logging.INFO ,
            * "WARNING" : logging.WARNING ,
            * "ERROR" : logging.ERROR ,
            * "CRITICAL" : logging.CRITICAL ,
        :return:
        """
        _stream_handler = logging.StreamHandler()
        _stream_handler.setLevel(self.levels[level])
        _stream_handler.setFormatter(self.formatter)
        self.log.addHandler(_stream_handler)
        return self.log

    def file_handler(self, file_name, mode):
        """

        :param file_name: ~.txt / ~.log
        :param mode: "w" / "a"
        :return:
        """
        _file_handler = logging.FileHandler(file_name, mode=mode)
        _file_handler.setLevel(logging.DEBUG)
        _file_handler.setFormatter(self.formatter)
        self.log.addHandler(_file_handler)
        return self.log

    def file_rotating_handler(self, file_name, mode, level, backup_count, log_max_size):
        """

        :param file_name: file의 이름 , ~.txt / ~.log
        :param mode: "w" / "a"
        :param backup_count: backup할 파일 개수
        :param log_max_size: 한 파일당 용량 최대
        :param level:

        > "DEBUG" : logging.DEBUG ,
        > "INFO" : logging.INFO ,
        > "WARNING" : logging.WARNING ,
        > "ERROR" : logging.ERROR ,
        > "CRITICAL" : logging.CRITICAL ,
        :return:
        """

        _file_handler = logging.handlers.RotatingFileHandler(
            filename=file_name,
            maxBytes=log_max_size,
            backupCount=backup_count,
            mode=mode)
        _file_handler.setLevel(self.levels[level])
        _file_handler.setFormatter(self.formatter)
        self.log.addHandler(_file_handler)
        return self.log

    def time_rotate_handler(self,
                            filename='./log.txt',
                            when="M",
                            level="DEBUG",
                            backup_count=4,
                            atTime=datetime.time(0, 0, 0),
                            interval=1):
        """
        :param level:
        :param filename:
        :param when: 저장 주기
        :param interval: 저장 주기에서 어떤 간격으로 저장할지
        :param backup_count: 5
        :param atTime: datetime.time(0, 0, 0)
        :return:
        """
        _file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=filename,
            when=when,  # W0
            backupCount=backup_count,
            interval=interval,
            atTime=atTime)
        _file_handler.setLevel(self.levels[level])
        _file_handler.setFormatter(self.formatter)
        self.log.addHandler(_file_handler)
        return self.log


class AppLogger:
    """

    AppLogger

    :param app_name: application name(=file name)
    :param log_level: log level
    :param log_path: log file path
    :param stdout: Enable stdout, Adding Hook for another library logging.
    :param markup: Enable markup for stdout logging.
    :param stdout_level: stdout log level
    :param stdout_log_formatter: stdout log formatter (function)
    :param log_format: log format / [%(asctime)s] %(name)s::" "%(filename)s/%(funcName)s(%(lineno)d) %(message)s
    :param use_hook_exception: Select whether to log exception errors.
    :param exception_handler: Exception handling function
    :param debug:

    Example:

        .. code-block:: python

            from pawnlib.utils import log

            app_logger, error_logger = log.AppLogger().get_logger()
            app_logger.info("This is a info message")
            error_logger.error("This is a info message")


    Example2:

        .. code-block:: python

            from pawnlib.config.globalconfig import pawnlib_config as pawn

            app_logger, error_logger = log.AppLogger(
                app_name="app",
                log_path="./logs",
                stdout=True
            ).set_global()

            pawn.app_logger.info("This is a info message")
            pawn.error_logger.error("This is a error message")

            # >>>
            [2022-07-25 18:52:44,415] INFO::app_logging_test.py/main(38) This is a info message
            [2022-07-25 18:52:44,416] ERROR::app_logging_test.py/main(39) This is a info message


    """
    _logger = None

    def __init__(self,
                 app_name: str = "default",
                 log_level: Literal["INFO", "WARN", "DEBUG"] = "INFO",
                 log_path: str = "./logs",
                 markup: bool = True,
                 stdout: bool = False,
                 stdout_level: Literal["INFO", "WARN", "DEBUG", "NOTSET"] = "INFO",
                 stdout_log_formatter: Callable = "%H:%M:%S,%f",
                 log_format: str = None,
                 debug: bool = False,
                 use_hook_exception: bool = True,
                 exception_handler: Callable = "",
                 **kwargs
                 ):
        self.app_name = app_name
        self.log_path = log_path
        self.debug = debug
        self.stdout = stdout
        self.stdout_level = stdout_level
        self.stdout_log_formatter = stdout_log_formatter
        self.markup = markup
        self.log_level = log_level
        self.use_hook_exception = use_hook_exception
        self.kwargs = kwargs

        if self.use_hook_exception:
            if exception_handler:
                sys.excepthook = exception_handler
            else:
                sys.excepthook = self.handle_exception

        if log_format:
            self.log_format = log_format
        else:
            self.log_format = "[%(asctime)s] %(name)s::" "%(filename)s/%(funcName)s(%(lineno)d) %(message)s"

        self.log_formatter = logging.Formatter(self.log_format)

        self._logger = self.set_logger(self.log_level)
        self._error_logger = self.set_logger("ERROR")

    def get_realpath(self):
        path = os.path.dirname(os.path.abspath(__file__))
        parent_path = os.path.abspath(os.path.join(path, ".."))
        return parent_path

    def set_logger(self, log_type="INFO"):
        # log_path = f"{self.get_realpath()}/logs"
        # print(f"log_path={self.log_path}")
        if not os.path.isdir(self.log_path):
            os.mkdir(self.log_path)

        _logger = logging.getLogger(log_type)
        stack = traceback.extract_stack()
        _logger.setLevel(getattr(logging, log_type))

        if log_type == "ERROR":
            filename = f"{self.app_name}.{str(log_type).lower()}.log"
        else:
            filename = f"{self.app_name}.log"

        logfile_filename = "%s/%s" % (self.log_path, filename)

        file_handler = self.time_rotate_handler(
            filename=logfile_filename,
            when='midnight',
            interval=1,
            encoding='utf-8',
            backup_count=10
        )
        file_handler.suffix = '%Y%m%d'
        file_handler.setFormatter(self.log_formatter)
        _logger.addHandler(file_handler)

        if self.stdout:
            if self.stdout_log_formatter:
                log_time_formatter = lambda dt: Text.from_markup(f"[{dt.strftime(self.stdout_log_formatter)[:-3]}]")
            else:
                log_time_formatter = None
            # if self.stdout_log_formatter:
            #
            # else:
            #     log_time_formatter = lambda dt: Text.from_markup(f"[{dt.strftime('%H:%M:%S,%f')[:-3]}]")

            logging.basicConfig(
                # level=self.stdout_level, format="%(message)s", datefmt="[%Y-%m-%d %H:%M:%S.%f]", handlers=[RichHandler(rich_tracebacks=True)]
                level=self.stdout_level,
                format="%(message)s",
                handlers=[
                    TightLevelRichHandler(
                        rich_tracebacks=True,
                        log_time_format=log_time_formatter,
                        markup=self.markup,
                        **self.kwargs
                    )
                ]
            )
        # _logger.addHandler(self.add_stream_handler(level=log_type))
        return _logger

    def add_stream_handler(self, level):
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(self.log_formatter)
        return stream_handler

    def time_rotate_handler(self,
                            filename='./log.txt',
                            when="M",
                            backup_count=4,
                            atTime=datetime.time(0, 0, 0),
                            interval=1,
                            encoding="utf-8"
                            ):
        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=filename,
            when=when,  # W0
            backupCount=backup_count,
            interval=interval,
            atTime=atTime,
            encoding=encoding
        )
        return file_handler

    def get_logger(self):
        """
        Get the logger

        :return:
        """
        return self._logger, self._error_logger

    def set_global(self):
        """
        Add global config in pawnlib

        :return:
        """
        pawnlib_config.set(
            PAWN_APP_LOGGER=self._logger,
            PAWN_ERROR_LOGGER=self._error_logger,
        )

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        if self.use_hook_exception and self._error_logger:
            self._error_logger.error("Unexpected exception", exc_info=(exc_type, exc_value, exc_traceback))


class TightLevelRichHandler(RichHandler):
    def get_level_text(self, record) -> Text:
        """Get the level name from the record.

        Args:
            record (LogRecord): LogRecord instance.

        Returns:
            Text: A tuple of the style and level name.
        """
        display_level_count = 3
        level_name = record.levelname

        short_level_name = record.levelname[0:display_level_count]

        level_text = Text.styled(
            short_level_name.ljust(display_level_count), f"logging.level.{level_name.lower()}"
        )
        return level_text
