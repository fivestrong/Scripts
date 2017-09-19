#! /usr/bin/env python
# _*_ coding:utf-8 _*_
import argparse

def readfile(filename):
    '''print a file to standard output'''
    with open(filename) as f:
        file_data = f.read()
    return file_data

def get_args():
    parser = argparse.ArgumentParser(
        description="A simple python script for cat command",
        epilog="python cat.py [filename]"
    )

    # required argument 
    parser.add_argument("filenames", nargs='*', help="the filename that you want to display")  
    return parser.parse_args()

if __name__ == '__main__':
   files = get_args().filenames
   content = ''
   for filename in files:
       content = content + readfile(filename)
   print(content)
