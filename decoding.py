import os
import sys
from color_state import State


def decode(states):
    text = ""
    for i in range(0, len(states), 2):
        bits = [states[i].r, states[i].g, states[i].b, states[i].y]
        bits += [states[i+1].r, states[i+1].g, states[i+1].b, states[i+1].y]

        s = ""
        for i in range(len(bits)):
            s += str(bits[i])
        val = int(s, 2)
        text += str(chr(val))

        # print(num)

    return text


if __name__ == '__main__':
    states = [State(r=0, g=1, b=0, y=0, w=1), State(r=0, g=0, b=0, y=1, w=1)]
    text = decode(states)
    f = open("output.txt", "w")
    f.write(text)
    f.close()
