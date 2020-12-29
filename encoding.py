import os
import sys
from color_state import State
from bitarray import bitarray


def encode(f):
    states = []
    byte = f.read(1)
    while byte:
        b = ord(byte)
        m = 1
        bits = []
        for i in range(0, 8):
            bits.append(int((m & b) != 0))
            m = m << 1
        bits.reverse()

        #parity1 = int(((bits[0] + bits[1] + bits[2] + bits[3]) % 2 == 1))
        #parity2 = int(((bits[4] + bits[5] + bits[6] + bits[7]) % 2 == 1))
        S1 = State(bits[0], bits[1], bits[2], bits[3], 0)
        S2 = State(bits[4], bits[5], bits[6], bits[7], 0)
        states.append(S1)
        states.append(S2)

        byte = f.read(1)
    return states


if __name__ == '__main__':
    f = open(os.path.abspath("test.txt"), "rb")
    states = encode(f)
    print(states)
