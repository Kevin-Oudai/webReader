"""Command line interface for the text reader."""

import argparse
import logging

from Reader import Reader


def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""

    parser = argparse.ArgumentParser(description="Read a text file page by page")
    parser.add_argument("--file", "-f", dest="file_path", required=True,
                        help="Path to the text file to read")
    parser.add_argument("--goto", "-g", dest="goto", type=int,
                        help="Jump to a specific page number (0-indexed)")
    parser.add_argument("--reset", action="store_true",
                        help="Reset stored reading position for the file")
    parser.add_argument("--page-size", type=int,
                        help="Number of lines to show per page")
    return parser.parse_args()


def main() -> None:
    """Entry point for the command line interface."""

    logging.basicConfig(level=logging.INFO)
    args = parse_args()
    reader = Reader(args.file_path, page_size=args.page_size or Reader.page_size)

    if args.reset:
        reader.reset()

    if args.goto is not None:
        try:
            reader.goto(args.goto)
        except ValueError as exc:
            print(f"Error: {exc}")
            return

    try:
        while True:
            print(reader.read())
            if reader.current_page >= len(reader.pages):
                break
            command = input("Press Enter for next page or 'q' to quit: ").strip().lower()
            if command == 'q':
                break
    except FileNotFoundError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()

