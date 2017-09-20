import os
import argparse
import glob

showlist = []

def dirList(path):
    flist = os.listdir(path)
    for file in flist:
        fpath = os.path.join(path, file)
        if os.path.isdir(fpath):
            dirList(fpath)
        showlist.append(fpath)
    return showlist

def get_args():
    parser = argparse.ArgumentParser(
        description="A simple python script for find command",
        epilog="python find.py dirpath [-name ] [-exec ]"
    )

    parser.add_argument(dest="path", metavar='dirpath', type=str, help="input the dirpath you want to find for")
    parser.add_argument('-n', '--name', help='the name you want to find')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    if not args.name:
        for i in dirList(args.path):
            print(i)
    else:
        for file in  os.listdir(args.path):
            fpath = os.path.join(args.path, file)
            if os.path.isdir(fpath):
                os.chdir(fpath)
                for i in glob.glob(args.name):
                    print(i)





            

