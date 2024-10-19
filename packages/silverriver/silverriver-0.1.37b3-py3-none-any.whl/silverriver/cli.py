import argparse
import logging
from urllib.parse import urlparse

from silverriver import upload_trace, record_trace
from silverriver.utils.auth import store_silverriver_key

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger()


def valid_url(url: str) -> str:
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ('http', 'https') or not parsed_url.netloc:
        raise argparse.ArgumentTypeError(f"Invalid URL: {url}, must start with http:// or https://")

    return url


def auth_cli(args):
    store_silverriver_key(args.api_key)


def upload_trace_cli(args):
    upload_trace(args.trace_file)


def record_trace_cli(args):
    trace_file = record_trace(args.url, args.output)

    if args.upload:
        args.trace_file = trace_file
        upload_trace_cli(args)


def main():
    parser = argparse.ArgumentParser(description="SilverRiver CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    # Setup command
    login_parser = subparsers.add_parser("auth", help="Authenticate and store the API key locally", )
    login_parser.add_argument('--api-key', help='Your unique API key for authentication', required=True,
                              metavar='KEY')

    login_parser.set_defaults(func=auth_cli)

    # Record command
    record_parser = subparsers.add_parser("record", help="Record a new trace")
    record_parser.add_argument('url', help='The URL of the webpage to trace', type=valid_url)
    record_parser.add_argument('-o', '--output', default='silverriver_trace',
                               help='The output filename for the trace (output will be a zipped file)')
    record_parser.add_argument('--upload', action='store_true', help='Upload the trace after recording')
    record_parser.set_defaults(func=record_trace_cli)

    # Upload command
    upload_parser = subparsers.add_parser("upload", help="Upload an existing trace")
    upload_parser.add_argument('trace_file', help='The trace file to upload')
    upload_parser.set_defaults(func=upload_trace_cli)

    args = parser.parse_args()

    if args.command:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
