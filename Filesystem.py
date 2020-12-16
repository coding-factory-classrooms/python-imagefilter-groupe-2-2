import os.path
from os import path

def isFileValid(filepath):
    if path.exists(filepath) == True:
        return True

    else :
        return False