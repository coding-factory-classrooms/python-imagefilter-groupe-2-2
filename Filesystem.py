import os.path
from os import path


def isFileValid(filepath):
    if path.exists(filepath):
        return True

    else:
        return False
