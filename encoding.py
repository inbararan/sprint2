import os
import sys
def encode(f):
    byte = f.read(1)
    mask = 0b1
    bits = []
    for i in range(0, 8):
        b = ((mask & byte) != 0)
        bits.append(b)


if __name__ == '__main__':
    f = open(os.path.abspath(sys.argv[1]), "rb")
    encode(f)