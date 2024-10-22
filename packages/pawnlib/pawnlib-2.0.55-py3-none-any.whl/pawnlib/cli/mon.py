#!/usr/bin/env python3
import os
import asyncio
import argparse
from aiohttp import ClientSession
from dotenv import load_dotenv, find_dotenv
from pawnlib.config import pawn
from pawnlib.builder.generator import generate_banner
from pawnlib.__version__ import __version__ as _version
from pawnlib.resource.monitor import SSHMonitor
from pawnlib.input.prompt import CustomArgumentParser, ColoredHelpFormatter
from typing import List, Dict, Optional, Type, Any
from pawnlib.typing import (
    hex_to_number,
    shorten_text,
    str2bool,
    is_valid_token_address,
)
from pawnlib.output import print_var, get_script_path, is_file
from pawnlib.utils.http import AsyncGoloopWebsocket


__description__ = "SSH and Wallet Monitoring Tool"
__epilog__ = (
    "\nUsage examples:\n\n"
    "1. Start monitoring SSH log files:\n"
    "     `pawns mon ssh -f /var/log/secure /var/log/auth.log`\n\n"
    "2. Start the wallet client:\n"
    "     `pawns mon wallet --url https://example.com -vvv`\n\n"
    "Note:\n"
    "  You can monitor multiple log files by providing multiple `-f` arguments.\n"
)

def get_parser():
    parser = CustomArgumentParser(
        description='Command Line Interface for SSH and Wallet Monitoring',
        formatter_class=ColoredHelpFormatter,
        epilog=__epilog__
    )
    parser = get_arguments(parser)
    return parser


def add_common_arguments(parser):
    """Add common arguments to both SSH and Wallet parsers."""
    parser.add_argument(
        '--log-type',
        choices=['console', 'file'],
        default='console',
        help='Choose logger type: console or file (default: console)'
    )
    parser.add_argument(
        '--log-file',
        help='Log file path if using file logger (required if --log-type=file)',
        default=None
    )
    parser.add_argument(
        '-v',
        '--verbose',
        action='count',
        default=0,
        help='Increase verbosity level. Use -v, -vv, -vvv, etc.'
    )
    parser.add_argument(
        '--slack-webhook-url',
        help='Slack webhook URL',
        default=None
    )
    parser.add_argument(
        '--send-slack',
        type=str2bool,
        help='Enable sending messages to Slack',
        default=True
    )

    parser.add_argument(
        '--priority',
        choices=['env', 'args'],
        default='args',
        help='Specify whether to prioritize environment variables ("env") or command-line arguments ("args"). Default is "args".'
    )

    return parser


def get_arguments(parser=None):
    if not parser:
        parser = CustomArgumentParser()

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    ssh_parser = subparsers.add_parser('ssh', help='Monitor SSH logs')
    ssh_parser.add_argument(
        '-f', '--file',
        metavar='log_file',
        help='SSH log file(s) to monitor',
        nargs='+',
        default=['/var/log/secure']
    )
    ssh_parser.add_argument(
        '-b', '--base-dir',
        metavar='base_dir',
        help='Base directory for the application',
        default="."
    )
    add_common_arguments(ssh_parser)

    wallet_parser = subparsers.add_parser('wallet', help='Run the Async Goloop Websocket Client')
    wallet_parser.add_argument(
        '--url',
        help='Endpoint URL',
    )
    wallet_parser.add_argument(
        '--ignore-data-types',
        help='Comma-separated list of data types to ignore',
        default='base'
    )
    wallet_parser.add_argument(
        '--check-tx-result-enabled',
        type=str2bool,
        help='Enable checking transaction results',
        default=True
    )
    wallet_parser.add_argument(
        '--address-filter',
        help='Comma-separated list of addresses to filter',
        default=None
    )
    wallet_parser.add_argument(
        '--max-transaction-attempts',
        type=int,
        help='Maximum transaction attempts',
        default=10
    )
    add_common_arguments(wallet_parser)
    return parser


# def load_environment_settings(args):
#     """
#     Load environment settings from environment variables or .env file.
#     """
#     def get_list_from_env(key, default=""):
#         """Helper function to get list from environment variable."""
#         # return os.environ.get(key, default).split(",") if os.environ.get(key) else []
#         return [item.strip() for item in os.environ.get(key, default).split(",") if item] if os.environ.get(key) else []
#
#     return {
#             'url': os.environ.get('ENDPOINT_URL', ""),
#             # 'ignore_data_types': os.environ.get('IGNORE_DATA_TYPES', "base").split(","),
#             'ignore_data_types': get_list_from_env('IGNORE_DATA_TYPES', None),
#             'check_tx_result_enabled': str2bool(os.environ.get('CHECK_TX_RESULT_ENABLED', None)),
#             # 'address_filter': os.environ.get('ADDRESS_FILTER', "").split(',') if os.environ.get('ADDRESS_FILTER') else [],
#             'address_filter': get_list_from_env('ADDRESS_FILTER', []),
#             'log_type': os.environ.get('LOG_TYPE', None),
#             "file": get_list_from_env('FILE', None),
#             'slack_webhook_url': os.environ.get('SLACK_WEBHOOK_URL', None),
#             'send_slack': str2bool(os.environ.get('SEND_SLACK', getattr(args, "max_transaction_attempts", None))),
#             'max_transaction_attempts': int(os.environ.get('MAX_TRANSACTION_ATTEMPTS', getattr(args, "max_transaction_attempts", 3))),
#             'verbose': int(os.environ.get('VERBOSE', getattr(args, "verbose", 0)))
#         }

def load_environment_settings(args) -> dict:
    """
    Load environment settings from command-line arguments or environment variables,
    prioritizing args if provided, otherwise using environment variables.
    """
    import os

    def get_setting(
            attr_name: str,
            env_var: str,
            default: Optional[Any] = None,
            value_type: Type = str,
            is_list: bool = False
    ) -> Any:
        """Helper function to get setting value from args or env."""
        # First, try to get from args
        value = getattr(args, attr_name, None)
        if value is not None:
            return value

        # If not in args, try environment variable
        env_value = os.environ.get(env_var, None)
        if env_value is not None:
            if is_list:
                return [item.strip() for item in env_value.split(",") if item.strip()]
            elif value_type == bool:
                return str2bool(env_value)
            elif value_type == int:
                try:
                    return int(env_value)
                except ValueError:
                    return default
            else:
                return env_value

        # If neither, return default
        return default

    settings: dict = {
        'url': get_setting('url', 'ENDPOINT_URL', default="", value_type=str),
        'ignore_data_types': get_setting('ignore_data_types', 'IGNORE_DATA_TYPES', default=['base'], is_list=True),
        'check_tx_result_enabled': get_setting('check_tx_result_enabled', 'CHECK_TX_RESULT_ENABLED', default=True, value_type=bool),
        'address_filter': get_setting('address_filter', 'ADDRESS_FILTER', default=[], is_list=True),
        'log_type': get_setting('log_type', 'LOG_TYPE', default='console', value_type=str),
        'file': get_setting('file', 'FILE', default=None, is_list=True),
        'slack_webhook_url': get_setting('slack_webhook_url', 'SLACK_WEBHOOK_URL', default=None, value_type=str),
        'send_slack': get_setting('send_slack', 'SEND_SLACK', default=True, value_type=bool),
        'max_transaction_attempts': get_setting('max_transaction_attempts', 'MAX_TRANSACTION_ATTEMPTS', default=3, value_type=int),
        'verbose': get_setting('verbose', 'VERBOSE', default=0, value_type=int)
    }

    return settings


def setup_app_logger(log_type: str = 'console', verbose: int = 0, app_name: str = ""):
    """Sets up the logger based on the selected type (console or file)."""
    log_time_format = '%Y-%m-%d %H:%M:%S.%f'

    if log_type == 'file':
        pawn.set(
            PAWN_LOGGER=dict(
                log_level="INFO",
                stdout_level="INFO",
                stdout=verbose > 0,
                use_hook_exception=True,
            ),
            PAWN_TIME_FORMAT=log_time_format,
            PAWN_CONSOLE=dict(
                redirect=True,
                record=True
            ),
            app_name=app_name,
            data={}
        )
        logger = pawn.app_logger
    else:
        logger = pawn.console  # Use pawn's built-in console logger
    return logger


def initialize_logger(args):
    """Set up the logger based on the command and its log type."""
    app_name = f"{args.command}_watcher"
    return setup_app_logger(log_type=args.log_type, verbose=args.verbose, app_name=app_name)


# def merge_environment_settings(args):
#     dotenv_path = f"{pawn.get_path()}/.env"
#     if not is_file(dotenv_path):
#         pawn.console.log(".env file not found")
#     else:
#         pawn.console.log(f".env file found at '{dotenv_path}'")
#         load_dotenv(dotenv_path=dotenv_path)
#     env_settings = load_environment_settings()
#
#     print(env_settings)
#
#     settings = env_settings.copy()
#     args_dict = vars(args)
#     _settings = {}
#
#     for key, value in args_dict.items():
#         # Use the value from args if it exists and is not None, otherwise fallback to env settings
#         pawn.console.log(key, value)
#         _settings[key] = value if value is not None else settings.get(key)
#     return _settings


def merge_environment_settings(args):
    """
    Merge environment settings with command-line arguments based on the selected priority.
    """
    dotenv_path = f"{pawn.get_path()}/.env"
    if not is_file(dotenv_path):
        pawn.console.log(".env file not found")
    else:
        pawn.console.log(f".env file found at '{dotenv_path}'")
        load_dotenv(dotenv_path=dotenv_path)

    # Load environment settings
    env_settings = load_environment_settings(args)

    # Merge settings based on priority
    args_dict = vars(args)
    settings = env_settings.copy()  # Start with environment settings
    _settings = {}

    # Determine which to prioritize: env or args
    if args.priority == 'env':
        # Environment variables take priority
        for key, value in args_dict.items():
            # Use the value from env if available, else fallback to args
            _settings[key] = env_settings.get(key, value)
    else:
        # Command-line arguments take priority
        for key, value in args_dict.items():
            if value is not None:
                _value = value
            else:
                _value = env_settings.get(key, value)
            # Use the value from args if provided, else fallback to env
            # pawn.console.log(key, value, _value)
            _settings[key] = _value
    return _settings



def run_monitor_ssh(args, logger):
    settings = merge_environment_settings(args)
    print_var(settings)

    ssh_monitor = SSHMonitor(
        log_file_path=settings.get('file'),
        slack_webhook_url=settings.get('slack_webhook_url'),
        alert_interval=60,
        verbose=settings.get('verbose', 0),
        logger=logger
    )

    async def run_async_monitor():
        await ssh_monitor.monitor_ssh()

    try:
        loop = asyncio.get_running_loop()
        loop.create_task(run_async_monitor())
        loop.run_forever()
    except RuntimeError:
        asyncio.run(run_async_monitor())

# def run_monitor_ssh(args, logger):
#     settings = merge_environment_settings(args)
#     print_var(settings)
#
#     ssh_monitor = SSHMonitor(
#         log_file_path=args.file,
#         slack_webhook_url=settings.get('slack_webhook_url'),
#         alert_interval=60,
#         verbose=settings.get('verbose', 0),
#         logger=logger
#     )
#     asyncio.run(ssh_monitor.monitor_ssh())


def run_wallet_client(args, logger):
    settings = merge_environment_settings(args)

    if not settings['url']:
        print("[ERROR] Endpoint URL is required. Please provide it via '--url' argument or 'ENDPOINT_URL' environment variable.")
        exit(1)

    settings_uppercase = {key.upper(): value for key, value in settings.items()}
    pawn.console.log("[INFO] Settings loaded from environment variables and command-line arguments.")
    pawn.console.log("Effective settings:\n")
    print_var(settings_uppercase)

    # Initialize AsyncGoloopWebsocket client
    # Run the WebSocket client
    async def run_client():
        async with ClientSession() as session:
            websocket_client = AsyncGoloopWebsocket(
                url=settings['url'],
                verbose=int(settings['verbose']),
                ignore_data_types=settings['ignore_data_types'],
                check_tx_result_enabled=settings['check_tx_result_enabled'],
                address_filter=settings['address_filter'],
                send_slack=settings['send_slack'],
                max_transaction_attempts=int(settings['max_transaction_attempts']),
                slack_webhook_url=settings['slack_webhook_url'],
                logger=logger,
                session=session
            )
            await websocket_client.initialize()
            await websocket_client.run()

    try:
        loop = asyncio.get_running_loop()
        loop.create_task(run_client())
        loop.run_forever()
    except RuntimeError:
        asyncio.run(run_client())


def main():
    banner = generate_banner(
        app_name="Monitoring",
        author="jinwoo",
        description="Monitor SSH logs and run the Async Goloop Websocket Client",
        font="ogre",
        version=_version
    )

    parser = get_parser()
    args = parser.parse_args()

    print(banner)
    pawn.console.log(f"Parsed arguments: {args}")

    if args.command:
        logger = initialize_logger(args)
    else:
        logger = None

    if args.command == "ssh":
        pawn.console.log(f"Starting SSH monitoring with files: {args.file}")
        run_monitor_ssh(args, logger)
    elif args.command == "wallet":
        pawn.console.log("Starting Async Goloop Websocket Client")
        run_wallet_client(args, logger)
    else:
        parser.print_help()

main.__doc__ = (
    f"{__description__}\n{__epilog__}"
)

if __name__ == '__main__':
    main()
