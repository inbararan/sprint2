from arduino import set_state
from color_state import State
from encoding import encode
import time
import os

FOLDER = r"C:\Users\t8747262\Desktop\dest"

SLEEP_LEN = 1

stateAll = State(1, 1, 1, 1, 1)
stateOne = State(0, 0, 0, 0, 1)
stateNone = State(0, 0, 0, 0, 0)

set_state(stateNone)

input("Press enter to light up\n")

set_state(stateAll)
time.sleep(30)

print("Ready for files")
done_files = []


def relevant_files():
    return list(filter(lambda fn: fn not in done_files, os.listdir(FOLDER)))


while True:
    files = []
    while len(files) == 0:
        files = relevant_files()

    for file_name in files:
        print(f"Handling {file_name}")
        done_files.append(file_name)

        with open(os.path.join(FOLDER, file_name), "rb") as f:
            states = encode(f)

        for state in states:
            set_state(stateOne)
            time.sleep(SLEEP_LEN)
            set_state(state)
            time.sleep(SLEEP_LEN)

        set_state(stateAll)
        time.sleep(2)
        set_state(stateNone)
