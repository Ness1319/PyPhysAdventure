# This file manages saves
import os
import glob
import shutil
from bin import type


def new(name):
    # Reformat the name of the new file
    str(name)
    name = name.lower()
    if name == "":
        name = "unnamed"

    # Check if file already exists

