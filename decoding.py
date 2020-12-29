import os
import sys
from color_state import State


def decode(states):
    states = []
    byte = f.read(1)
    while not byte:
        mask = 0b1
        bits = []
        for i in range(0, 8):
            b = ((mask & byte) != 0)
            bits.append(b)

        xor1 = bits[0] ^ bits[1] ^ bits[2] ^ bits[3]
        xor2 = bits[4] ^ bits[5] ^ bits[6] ^ bits[7]
        S1 = State(bits[0], bits[1], bits[2], bits[3], xor1)
        S2 = State(bits[4], bits[5], bits[6], bits[7], xor2)
        states.append(S1)
        states.append(S2)

        byte = f.read(1)
    return states

def decode(states):
    i = 0

    while i < len(states)
    S1 = states[i]
    i += 1
    S2 = states[i]



    i += 1


if __name__ == '__main__':
    states = []
    text = decode(states)
