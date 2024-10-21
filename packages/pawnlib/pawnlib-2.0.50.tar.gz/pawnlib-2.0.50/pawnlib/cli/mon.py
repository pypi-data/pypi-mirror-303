#!/usr/bin/env python3
import os
import asyncio
import argparse
from dotenv import load_dotenv
from pawnlib.config import pawn
from pawnlib.output import color_print
from pawnlib.builder.generator import generate_banner
from pawnlib.__version__ import __version__ as _version
from pawnlib.resource.monitor import SSHMonitor
from pawnlib.input.prompt import CustomArgumentParser, ColoredHelpFormatter
from pawnlib.typing import (
    hex_to_number,
    shorten_text,
    str2bool,
    is_valid_token_address,
)
from pawnlib.output import print_var
from pawnlib.utils.http import AsyncGoloopWebsocket  # Import AsyncGoloopWebsocket


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

    wallet_parser = subparsers.add_parser('wallet', help='Run the Async Goloop Websocket Client')
    wallet_parser.add_argument(
        '--url',
        help='Endpoint URL',
        # required=True  # required를 제거합니다.
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
        '--slack-webhook-url',
        help='Slack webhook URL',
        default=None
    )
    wallet_parser.add_argument(
        '--send-slack',
        type=str2bool,
        help='Enable sending messages to Slack',
        default=True
    )
    wallet_parser.add_argument(
        '--max-transaction-attempts',
        type=int,
        help='Maximum transaction attempts',
        default=10
    )
    wallet_parser.add_argument(
        '-v',
        '--verbose',
        action='count',
        default=0,
        help='Increase verbosity level. Use -v, -vv, -vvv, etc.'
    )
    return parser

def monitor_ssh(args):
    log_file_paths = args.file
    slack_webhook_url = os.getenv('SLACK_WEBHOOK_URL', '')

    ssh_monitor = SSHMonitor(
        log_file_path=log_file_paths,
        slack_webhook_url=slack_webhook_url,
        alert_interval=60,
    )

    async def run_async_monitor():
        await ssh_monitor.monitor_ssh()

    try:
        loop = asyncio.get_running_loop()
        loop.create_task(run_async_monitor())
        loop.run_forever()
    except RuntimeError:
        asyncio.run(run_async_monitor())


def load_environment_settings():
    """
    Load environment settings from environment variables or .env file.
    """
    return {
        'url': os.environ.get('ENDPOINT_URL', ""),
        'ignore_data_types': os.environ.get('IGNORE_DATA_TYPES', "base").split(","),
        'check_tx_result_enabled': str2bool(os.environ.get('CHECK_TX_RESULT_ENABLED', True)),
        'address_filter': os.environ.get('ADDRESS_FILTER', "").split(',') if os.environ.get('ADDRESS_FILTER') else [],
        'slack_webhook_url': os.environ.get('SLACK_WEBHOOK_URL', ""),
        'send_slack': str2bool(os.environ.get('SEND_SLACK', True)),
        'max_transaction_attempts': int(os.environ.get('MAX_TRANSACTION_ATTEMPTS', 10)),
        'verbose': int(os.environ.get('VERBOSE', 3))
    }

def run_wallet_client(args):
    # Load environment variables from .env file
    load_dotenv()
    env_settings = load_environment_settings()
    settings = env_settings.copy()
    for key in settings:
        if hasattr(args, key):
            value = getattr(args, key)
            if value is not None:
                settings[key] = value

    if not settings['url']:
        print("[ERROR] Endpoint URL is required. Please provide it via '--url' argument or 'ENDPOINT_URL' environment variable.")
        exit(1)

    settings_uppercase = {key.upper(): value for key, value in settings.items()}
    pawn.console.log("[INFO] Settings loaded from environment variables and command-line arguments.")
    pawn.console.log("Effective settings:\n")
    print_var(settings_uppercase)

    # Initialize AsyncGoloopWebsocket client
    websocket_client = AsyncGoloopWebsocket(
        url=settings['url'],
        verbose=int(settings['verbose']),
        ignore_data_types=settings['ignore_data_types'],
        check_tx_result_enabled=settings['check_tx_result_enabled'],
        address_filter=settings['address_filter'],
        send_slack=settings['send_slack'],
        max_transaction_attempts=int(settings['max_transaction_attempts']),
        slack_webhook_url=settings['slack_webhook_url'],
        logger=pawn.console
    )

    # Run the WebSocket client
    async def run_client():
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
        font="elite",
        version=_version
    )

    parser = get_parser()
    args = parser.parse_args()

    print(banner)
    pawn.console.log(f"Parsed arguments: {args}")

    if args.command == "ssh":
        pawn.console.log(f"Starting SSH monitoring with files: {args.file}")
        monitor_ssh(args)
    elif args.command == "wallet":
        pawn.console.log("Starting Async Goloop Websocket Client")
        run_wallet_client(args)
    else:
        parser.print_help()

main.__doc__ = (
    f"{__description__}\n{__epilog__}"
)

if __name__ == '__main__':
    main()
