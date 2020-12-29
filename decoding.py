import os
import sys
from color_state import State


def decode(states):
    for i in range(0, len(states), 2):
        bits = [states[i].r, states[i].g, states[i].b, states[i].y, states[i].w]
        bits += [states[i+1].r, states[i+1].g, states[i+1].b, states[i+1].y, states[i+1].w]

        print(bits)
        print(chr())
        m = 1
        num = 0
        s = ""
        for i in range(len(bits)):
            s += str(bits[i])
        val = int(s, 2)
        print(chr(val))
        for i in range(len(bits)):
            num += m * bits[len(bits)-i-1]
            m = m << 1
        # print(num)

    return states


if __name__ == '__main__':
    states = [State(r=0, g=1, b=0, y=0, w=1), State(r=0, g=0, b=0, y=1, w=1)]
    text = decode(states)
