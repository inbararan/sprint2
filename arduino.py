from color_state import State
from serial import Serial
import time

arduino = Serial('COM3', 9600)
time.sleep(2)  # a 2 seconds delay that initializes the connection


def set_state(s: State):
    arduino.write(bytes(f"{s.r}{s.g}{s.b}{s.y}{s.w}", "ascii"))
