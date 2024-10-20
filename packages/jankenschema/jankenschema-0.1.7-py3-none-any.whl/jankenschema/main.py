import argparse

from jankenschema import generate_code


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s", "--src", required=True, help="The path to the database file"
    )
    parser.add_argument(
        "-d", "--dest", required=True, help="The path to the destination folder"
    )
    parser.add_argument(
        "-e",
        "--ext",
        required=True,
        help="The code extension (e.g., .ts)",
        choices=["ts", "rs"],
    )
    return parser.parse_args()


def main():
    args = get_args()
    generate_code(args.src, args.dest, args.ext)
