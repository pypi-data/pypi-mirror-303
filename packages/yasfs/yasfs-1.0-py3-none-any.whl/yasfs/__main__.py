import os
import argparse
from yasfs.config import read_config_file, create_default_config


def main() -> None:
    args = parse_args()

    if args.use_current_dir:
        args.source = os.getcwd()
        args.destination = os.getcwd()
    
    start(args)

def start(args) -> None:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_directory, 'config.ini')

    if args.config:
        create_default_config(config_file_path)
        print(f"Opening config file at {config_file_path}")
        open_file_explorer(config_file_path)
        return

    read_config_file(config_file_path, args)

def parse_args():
    ap = argparse.ArgumentParser(allow_abbrev=False)
    ap.add_argument(
        "-s",
        "--source",
        type=str,
        required=False,
        help="Takes FilePath as value; determines where files are being read from"
    )
    ap.add_argument(
        "-d",
        "--destination",
        type=str,
        required=False,
        help="Takes FilePath as value; determines where files get moved to"
    )
    ap.add_argument(
        "-sf",
        "--subfolder_only_sort",
        action='store_true',
        required=False,
        help="If provided, does not sort files if they have no pre-made destination folder"
    )
    ap.add_argument(
        "-u",
        "--use_current_dir",
        action='store_true',
        required=False,
        help="If provided, it uses the current directory for both source and destination."
    )
    ap.add_argument(
        "-c",
        "--config",
        action='store_true',
        required=False,
        help="If provided, opens the config directory."
    )

    return ap.parse_args()

def open_file_explorer(path: str) -> None:
    """Open File Explorer (or Finder) to the specified directory."""
    if os.name == 'nt':  # Windows
        os.startfile(path)
    elif os.name == 'posix':  # macOS/Linux
        if os.system(f"xdg-open {path}") != 0:  # Linux with xdg-open
            os.system(f"open {path}")  # macOS open command