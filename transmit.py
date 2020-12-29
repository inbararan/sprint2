from arduino import set_state
from color_state import State
from encoding import encode
from decoding import decode
import time
import os
import sys


def blink():
    stateAll = State(1, 1, 1, 1, 1)
    stateNone = State(1, 1, 1, 1, 1)


f = open("test.txt", "r")
states = encode(f)

for state in states:
    time.sleep(0.4)
    set_state(state)
