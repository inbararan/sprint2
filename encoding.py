import os
import sys
def encode(f):
    text = f.read()



if __name__ == '__main__':
    f = open(os.path.abspath(sys.argv[1]))
    encode(f)