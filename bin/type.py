# This module contains the slow print function for the command line game
import time


def slowprint(text):
    str(text)
    for char in text:
        print(char, flush=True, end="")
        time.sleep(0.02)
    print("")
