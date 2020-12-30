from image_process_try import return_to_ophir
#from image_processing_advanced import return_to_ophir
from encoding import encode
from decoding import decode, decode_raw
from color_state import State
import time
import os
import sys

if __name__ == '__main__':
    states = return_to_ophir() #.split(State(2, 2, 2, 2, 2))
    #states = [g for g in states if len(g) > 0]

    text = decode(states) # decode(states[0])
    f = open("output.txt", "w")
    f.write(text)
    f.close()
    with open("big.txt", "w") as f:
        f.write(decode(states[1]))

    with open("output.bmp", "wb") as f:
        f.write(decode_raw(states[2]))

