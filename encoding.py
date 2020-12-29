import os
import sys
from color_state import State
from bitarray import bitarray


def andbytes(abytes, bbytes):
    return bytes([a & b for a, b in zip(abytes[::-1], bbytes[::-1])][::-1])


def encode(f):
    states = []
    byte = f.read(1)
    while byte:
        b = ord(bytes)
        m = ord(0b1)
        bits = []
        for i in range(0, 8):
            print(bytes(mask))
            print(bytes(mask)[0] & bytes(byte)[0])
            bits.append((bytes(mask)[0] & bytes(byte)[0]))
            mask = mask << 1
        print(bits)

        xor1 = bits[0] ^ bits[1] ^ bits[2] ^ bits[3]
        xor2 = bits[4] ^ bits[5] ^ bits[6] ^ bits[7]
        S1 = State(bits[0], bits[1], bits[2], bits[3], xor1)
        S2 = State(bits[4], bits[5], bits[6], bits[7], xor2)
        states.append(S1)
        states.append(S2)

        #byte = f.read(1)
        byte = None
    return states


if __name__ == '__main__':
    f = open(os.path.abspath("test.txt"), "rb")
    states = encode(f)
    print(states)
