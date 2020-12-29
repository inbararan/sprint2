from arduino import set_state
from encoding import encode
from decoding import decode
import time
import os
import sys

f = open("test.txt", "r")
states = encode(f)

for state in states:
    time.sleep(0.4)
    set_state(state)
