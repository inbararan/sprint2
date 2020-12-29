from arduino import set_state
from color_state import State
from encoding import encode
from decoding import decode
import time
import os
import sys

stateAll = State(1, 1, 1, 1, 1)
stateOne = State(0, 0, 0, 0, 1)
stateNone = State(0, 0, 0, 0, 0)


"""def blink():
    set_state(stateAll)
    time.sleep(1)
    set_state(stateNone)
    time.sleep(1)


blink()"""

set_state(stateNone)

input("Press enter to light up\n")

set_state(stateAll)
time.sleep(30)

file_name = input("Enter file path\n")


f = open(os.path.abspath(file_name), "rb")
states = encode(f)

for state in states:
    set_state(stateOne)
    time.sleep(0.2)
    set_state(state)
    time.sleep(0.2)

set_state(stateAll)
time.sleep(2)
set_state(stateNone)

f.close()

