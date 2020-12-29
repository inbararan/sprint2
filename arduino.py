from color_state import State
from serial import Serial
import time

arduino = Serial('COM5', 9600)
time.sleep(2)  # a 2 seconds delay that initializes the connection


def set_state(state: State):
    serial_string = str(state.r)
    serial_string += str(state.g)
    serial_string += str(state.b)
    serial_string += str(state.y)
    serial_string += str(state.w)

    arduino.write(bytes(serial_string, "ascii"))
