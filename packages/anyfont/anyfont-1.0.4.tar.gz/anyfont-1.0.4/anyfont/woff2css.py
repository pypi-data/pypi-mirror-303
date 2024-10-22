import os
from os import listdir,getcwd
from os.path import isfile, join, abspath, splitext
import argparse
candidates = [
    ".woff2",
    ".woff"
]
def main(path):
    with open(os.path.join(path,"font.css"), "w") as css:
        for f in listdir(path):
            file = join(path,f)
            ext = splitext(file)[1]
            print(ext)
            if isfile(file) and ext in candidates: 
                css.write("@font-face")
                css.write("{")
                css.write(f"\n\tfont-family: '{f.split('.')[0].replace('-',' ')}';")
                css.write(f"\n\tsrc: url('{f}');")
                css.write("\n}\n")
def entry():
    current_directory = abspath(getcwd())
    parser = argparse.ArgumentParser(description="AnyFont v1")
    parser.add_argument("-d", type=str, help="directory to search")
    args = parser.parse_args()
    current_directory = os.path.abspath(os.getcwd())
    if bool(args.d):
        current_directory = args.d
    main(current_directory)
if __name__ == '__main__':
    entry()