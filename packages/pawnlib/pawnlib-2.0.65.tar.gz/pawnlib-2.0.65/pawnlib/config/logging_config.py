# logging_config.py (new module)
from pawnlib.config.globalconfig import pawnlib_config, pawn, Null
from pawnlib.typing.constants import const
from rich.console import Console
import logging
import re

try:
    from typing import Literal, Union
except ImportError:
    from typing_extensions import Literal, Union

# from rich.logging import RichHandler
# from rich.text import Text
# from typing import Callable

# from pawnlib.utils.log import ConsoleLoggerAdapter

class ConsoleLoggerAdapter:
    def __init__(
            self,
            logger: Union[logging.Logger, Console, Null, None] = None,
            logger_name: str = "",
            verbose: Union[bool, int] = False
    ):
        """
        Wrapper class to unify logging methods for logging.Logger and rich.Console.

        :param logger: The logger object (logging.Logger, rich.Console, or Null)
        :param logger_name: Name of the logger
        :param verbose: Verbosity level (bool or int).
                        If False: WARNING level (default)
                        If True: INFO level
                        If 1: INFO level
                        If 2: DEBUG level
        """
        # Determine log level based on verbose parameter using constants
        if isinstance(verbose, bool):
            verbose_int = int(verbose)
        elif isinstance(verbose, int):
            verbose_int = verbose
        else:
            verbose_int = 0  # Default to 0 if invalid type

        # Cap the verbose level to the max defined level
        max_verbose_level = max(const.VERBOSE_LEVELS.keys())

        if verbose_int > max_verbose_level:
            verbose_int = max_verbose_level

        self.log_level = const.VERBOSE_LEVELS.get(verbose_int, logging.DEBUG)
        self.verbose = verbose_int
        # level_name = logging.getLevelName(self.log_level)  # 'INFO'

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
            self.logger.setLevel(self.log_level)

    def _create_default_logger(self, logger_name="") -> logging.Logger:
        """
        Create a default logger if none is provided.
        """
        logger = logging.getLogger(logger_name)
        logger.propagate = False
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter("%(asctime)s <%(name)s> %(levelname)s - %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        logger.setLevel(self.log_level)
        return logger

    def _escape_non_tag_brackets(self, message: str) -> str:
        """
        Escape non-rich-tag '[' in the message without altering rich tags.

        :param message: The log message.
        :return: The message with non-rich-tag '[' escaped.
        """
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

    def _should_log(self, level_name: str) -> bool:
        """
        Check if a message should be logged based on the current logging level.
        """
        level_value = getattr(logging, level_name.upper(), logging.INFO)
        return level_value >= self.log_level

    def _log(self, message: str, level: str = "info"):
        """
        Internal method to handle logging for both Logger and Console.
        """
        level = level.lower()
        if not self._should_log(level):
            return

        stack_offset = self._get_stack_offset()

        if isinstance(self.logger, logging.Logger):
            getattr(self.logger, level, self.logger.info)(message, stacklevel=stack_offset)
        elif isinstance(self.logger, Console):
            message = self._escape_non_tag_brackets(message)  # Escape brackets in the message

            level_tags = {
                "critical": "[bold red]CRIT[/bold red]",
                "error": "[red]ERR [/red]",
                "warning": "[yellow]WARN[/yellow]",
                "info": "[cyan]INFO[/cyan]",
                "debug": "[green]DEBUG[/green]",
            }

            tag = level_tags.get(level, "[cyan]INFO[/cyan]")
            self.logger.log(f"{tag} {message}", _stack_offset=stack_offset)
        else:
            pass  # Do nothing if logger type is unknown

    def _get_stack_offset(self) -> int:
        # Return the appropriate stack offset
        return 3

    # Public methods for common logging levels
    def critical(self, message: str):
        self._log(message, "critical")

    def error(self, message: str):
        self._log(message, "error")

    def warn(self, message: str):
        self._log(message, "warning")

    def warning(self, message: str):
        self._log(message, "warning")

    def info(self, message: str):
        self._log(message, "info")

    def debug(self, message: str):
        self._log(message, "debug")

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

def setup_logger(logger=None, name: str = "", verbose: Union[bool, int] = False):
    return ConsoleLoggerAdapter(logger, name, verbose)
