import argparse
import subprocess
import webbrowser

from src.api import get_daily_problem_url
from src.utils import check_daily_problem


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_open = subparsers.add_parser("open")
    parser_open.add_argument("browser", nargs="?")

    parser_check = subparsers.add_parser("check")
    parser_check.add_argument("username")

    return parser.parse_args()


def main():
    args = parse_args()
    match args.command:
        case "open":
            url = get_daily_problem_url()
            if args.browser:
                subprocess.Popen([args.browser, url])
            else:
                webbrowser.open(url)

        case "check":
            check_daily_problem(args.username)


if __name__ == "__main__":
    main()
