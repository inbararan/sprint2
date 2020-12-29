from image_process_try import return_to_ophir
from encoding import encode
from decoding import decode
import time
import os
import sys

if __name__ == '__main__':
    states = return_to_ophir()
    text = decode(states)
    f = open("output.txt", "w")
    f.write(text)
    f.close()

