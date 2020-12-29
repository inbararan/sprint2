from arduino import set_state
from color_state import State
from encoding import encode
from decoding import decode
import time
import os
import sys

stateAll = State(1, 1, 1, 1, 1)
stateOne = State(0, 0, 0, 0, 1)


"""def blink():
    set_state(stateAll)
    time.sleep(1)
    set_state(stateNone)
    time.sleep(1)


blink()"""

set_state(State(0, 0, 0, 0, 0))


file_name = input()

set_state(stateAll)
time.sleep(5)

f = open(os.path.abspath(file_name), "rb")
states = encode(f)

for state in states:
    set_state(stateOne)
    time.sleep(0.2)
    set_state(state)
    time.sleep(0.2)

set_state(State(0, 0, 0, 0, 0))
