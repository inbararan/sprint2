from image_processing_ari import return_to_ophir
from encoding import encode
from decoding import decode
import time
import os
import sys

states = return_to_ophir()

text = decode(states)
f = open("output.txt", "w")
f.write(text)
f.close()