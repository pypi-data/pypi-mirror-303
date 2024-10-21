import argparse
import logging
from urllib.parse import urlparse

from silverriver import record_trace

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger()


def valid_url(url: str) -> str:
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ('http', 'https') or not parsed_url.netloc:
        raise argparse.ArgumentTypeError(f"Invalid URL: {url}, must start with http:// or https://")

    return url


def record_trace_cli(args):
    record_trace(args.url, args.output)


def main():
    parser = argparse.ArgumentParser(description="SilverRiver CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Record command
    record_parser = subparsers.add_parser("record", help="Record a new trace")
    record_parser.add_argument('url', help='The URL of the webpage to trace', type=valid_url)
    record_parser.add_argument('-o', '--output',
                               help='The output filename for the trace (output will be a zipped file)',
                               required=True)
    record_parser.set_defaults(func=record_trace_cli)

    args = parser.parse_args()

    if args.command:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
