#! /usr/bin/env python
# _*_ coding:utf-8 _*_
import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description="A simple python script for cat command",
        epilog="python cat.py [filename]"
    )

    # required argument 
    parser.add_argument(dest="filenames", metavar='filename', type=str, nargs='*', help="the filename that you want to display")
    parser.add_argument('-n', '--numbers', action='store_true', help='umber all output lines')
    return parser.parse_args()

if __name__ == '__main__':
   args = get_args()
   line_number = 1
#    print(">>> parsed args: ", args)
   for filename in args.filenames:
       with open(filename) as f:
            if args.numbers:
               for line in f.readlines():
                   print(f"\t{line_number}\t{line}", end="")
                   line_number += 1
            else:
                print(f.read())


               