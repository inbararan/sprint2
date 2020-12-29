from color_state import State
import arduino
import time

while True:
    arduino.set_state(State(1, 0, 0, 0, 0))
    time.sleep(0.1)
    arduino.set_state(State(0, 1, 0, 0, 0))
    time.sleep(0.1)
    arduino.set_state(State(0, 0, 1, 0, 0))
    time.sleep(0.1)
    arduino.set_state(State(0, 0, 0, 1, 0))
    time.sleep(0.1)
    arduino.set_state(State(0, 0, 0, 0, 1))
    time.sleep(0.1)
