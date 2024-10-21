# logging_config.py (new module)
from pawnlib.config.globalconfig import pawnlib_config, pawn, Null
from rich.console import Console
# from typing import Callable
# import re
# import inspect
import logging

try:
    from typing import Literal, Union
except ImportError:
    from typing_extensions import Literal, Union

# from rich.logging import RichHandler
# from rich.text import Text
# from typing import Callable

# from pawnlib.utils.log import ConsoleLoggerAdapter

class ConsoleLoggerAdapter:
    def __init__(self, logger: Union[logging.Logger, Console, Null], logger_name="", verbose: bool = False):
        """
        Wrapper class to unify logging methods for logging.Logger and rich.Console.

        :param logger: The logger object (logging.Logger or rich.Console)
        :param verbose: If True, set logging to DEBUG level.
        """
        self.verbose = verbose
        if isinstance(logger, ConsoleLoggerAdapter):
            self.logger = logger.logger
        else:
            self.logger = logger

        if self.logger is None:
            self.logger = self._create_default_logger(logger_name)
        elif isinstance(self.logger, Null):
            self.logger = pawn.console
            pawn.console.log("[red][ERROR][/red] Logger instance is Null. Using default logger.")

        if isinstance(self.logger, logging.Logger):
            self.logger.setLevel(logging.DEBUG if self.verbose else logging.INFO)

    def _create_default_logger(self, logger_name="") -> logging.Logger:
        """
        Create a default logger for the WebSocket client if none is provided.
        """
        logger = logging.getLogger(logger_name)
        logger.propagate = False
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s <%(name)s> %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.DEBUG if self.verbose > 0 else logging.INFO)
        return logger

    def _escape_all_brackets(self, message: str) -> str:
        """
        Escape all square brackets in the message.
        :param message: The log message.
        :return: The message with all square brackets escaped.
        """
        # Escape all [ and ] in the message
        message = message.replace("[", r"\[")
        return message

    def _escape_non_tag_brackets(self, message: str) -> str:
        """
        Escape non-rich-tag '[' in the message without altering rich tags.

        :param message: The log message.
        :return: The message with non-rich-tag '[' escaped.
        """
        import re

        VALID_RICH_TAGS = {
            'red', 'bold', 'green', 'blue', 'yellow', 'cyan', 'magenta', 'white', 'black',
            'italic', 'underline', 'blink', 'reverse', 'strike', 'dim',
            'blink2', 'conceal', 'crossed_out', 'default', 'frame', 'framed',
            'overline', 'encircle', 'shadow', 'outline', 'hidden', 'standout',
            'superscript', 'subscript', 'link', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            # Add more valid tags as needed
        }

        result = ''
        i = 0
        length = len(message)

        while i < length:
            if message[i] == '[':
                # Possible start of a tag
                tag_match = re.match(r'\[/?([a-zA-Z0-9 _-]+)\]', message[i:])
                if tag_match:
                    tag_content = tag_match.group(1)
                    # Check if all parts of the tag are valid
                    tag_parts = tag_content.split()
                    if all(part in VALID_RICH_TAGS for part in tag_parts):
                        # It's a valid rich tag, copy it as is
                        tag_text = tag_match.group(0)
                        result += tag_text
                        i += len(tag_text)
                    else:
                        # Not a valid rich tag, escape the '['
                        result += r'\['
                        i += 1
                else:
                    # Not a tag, escape the '['
                    result += r'\['
                    i += 1
            else:
                result += message[i]
                i += 1

        return result


    def _log(self, message: str, level: str = "info"):
        """
        Internal method to handle logging for both Logger and Console.
        """
        level = level.lower()
        stack_offset = self._get_stack_offset()

        if isinstance(self.logger, logging.Logger):
            getattr(self.logger, level, self.logger.info)(message, stacklevel=stack_offset)
        elif isinstance(self.logger, Console):
            # elif isinstance(self.logger, Console) :
            message = self._escape_non_tag_brackets(message)  # Escape brackets in the message

            if level == "debug":
                self.logger.debug(message, _stack_offset=4)
            else:
                level_tags = {
                    "info": "[cyan]INFO   [/cyan]",
                    "error": "[red]ERROR  [/red]",
                    "warn": "[yellow]WARN   [/yellow]",
                    "critical": "[bold red]CRITICAL[/bold red]",
                }
                tag = level_tags.get(level, "[cyan]INFO   [/cyan]")
                self.logger.log(f"{tag} {message}", _stack_offset=stack_offset)
        else:
            pass

    def _get_stack_offset(self) -> int:
        # 현재 함수가 호출된 스택 깊이
        # current_frame = inspect.currentframe()
        # _get_stack_offset() -> _log() -> logging 메서드 순으로 호출되므로, 3을 반환
        return 3

    # Public methods for common logging levels
    def info(self, message: str):
        self._log(message, "info")

    def error(self, message: str):
        self._log(message, "error")

    def warn(self, message: str):
        self._log(message, "warn")

    def debug(self, message: str):
        self._log(message, "debug")

    def critical(self, message: str):
        self._log(message, "critical")

    def __repr__(self):
        """
        Return a string representation of the ConsoleLoggerAdapter showing the type of logger used.
        """
        logger_type = self._get_logger_type(self.logger)
        return f"<ConsoleLoggerAdapter logger_type={logger_type}>"

    def _get_logger_type(self, logger):
        """
        Helper method to recursively determine the type of the logger.
        """
        if isinstance(logger, ConsoleLoggerAdapter):
            return self._get_logger_type(logger.logger)
        elif isinstance(logger, logging.Logger):
            return "Logger"
        elif isinstance(logger, Console):
            return "Console"
        elif isinstance(logger, Null):
            return "Null"
        else:
            return type(logger).__name__


def setup_logger(logger=None, name: str = "", verbose: bool = False):
    return ConsoleLoggerAdapter(logger, name, verbose)
