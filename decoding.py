import os
import sys
from color_state import State


def error_checking(bits, w):
    parity = int(((bits[0] + bits[1] + bits[2] + bits[3]) % 2 == 1))
    if parity != w:
        bits[3] = int((not bits[3]))
    return bits

def decode(states):
    text = ""
    for i in range(0, len(states), 2):
        bits1 = [states[i].r, states[i].g, states[i].b, states[i].y]
        bits2 = [states[i + 1].r, states[i + 1].g, states[i + 1].b, states[i + 1].y]

        """bits1 = error_checking(bits1, states[i].w)
        bits2 = error_checking(bits2, states[i + 1].w)"""
        bits = bits1 + bits2
        s = ""
        for i in range(len(bits)):
            s += str(bits[i])
        val = int(s, 2)
        text += str(chr(val))

        # print(num)

    return text

def decode_raw(states):
    bits = []
    for i in range(0, len(states), 2):
        bits1 = [states[i].r, states[i].g, states[i].b, states[i].y]
        bits2 = [states[i + 1].r, states[i + 1].g, states[i + 1].b, states[i + 1].y]

        """bits1 = error_checking(bits1, states[i].w)
        bits2 = error_checking(bits2, states[i + 1].w)"""
        bits.extend(bits1 + bits2)
    return bytes(bits)


if __name__ == '__main__':
    states = [State(r=0, g=1, b=0, y=0, w=1), State(r=0, g=0, b=0, y=1, w=1), State(r=0, g=1, b=0, y=0, w=1),
     State(r=0, g=0, b=1, y=0, w=1), State(r=0, g=1, b=0, y=0, w=1), State(r=0, g=0, b=1, y=1, w=0),
     State(r=0, g=1, b=0, y=0, w=1), State(r=0, g=1, b=0, y=0, w=1), State(r=0, g=1, b=0, y=0, w=1),
     State(r=0, g=1, b=0, y=1, w=0), State(r=0, g=1, b=0, y=0, w=1), State(r=0, g=1, b=1, y=0, w=0),
     State(r=0, g=1, b=0, y=0, w=1), State(r=0, g=1, b=1, y=1, w=1), State(r=0, g=0, b=1, y=1, w=0),
     State(r=0, g=0, b=0, y=1, w=1), State(r=0, g=0, b=1, y=1, w=0), State(r=0, g=0, b=1, y=0, w=1),
     State(r=0, g=0, b=1, y=1, w=0), State(r=0, g=0, b=1, y=1, w=0)]

    text = decode(states)
    f = open("output.txt", "w")
    f.write(text)
    f.close()
