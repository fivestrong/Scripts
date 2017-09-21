import sys
import argparse
from pathlib import Path

def get_args():
    parser = argparse.ArgumentParser(
        description="A simple python script for find command",
        epilog="python find.py dirpath [-name ] [-type ]"
    )

    parser.add_argument(dest="path", metavar='dirpath', type=str, help="input the dirpath you want to find for")
    parser.add_argument('-n', '--name', help='the name you want to find')
    parser.add_argument('-t', '--type', help="the file which type you want to find, use 'd' for directory, 'f' for file" )
    return parser.parse_args()

def name_find(start_path, args):
    for f in start_path.rglob(args.name):
        print(f)

def type_find(start_path, args):
    if args.type not in ['d', 'f']:
        print(f"Unkown type: {args.type}")
        sys.exit(1)

    for f in start_path.rglob(args.name or "*"):
        if args.type == "d" and f.is_dir():
            print(f)
        elif args.type == "f" and f.is_file():
            print(f)


def find_files(args):
    start_path = Path(args.path)

    if args.name and not args.type:
        name_find(start_path, args)
    elif args.type:
        type_find(start_path, args)
    else:
        print("You need either --name or --type")
        sys.exit(1)


if __name__ == '__main__':
    find_files(get_args())






            

