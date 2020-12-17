import os
from os import path
def create_directory(output):
    if not path.exists(output):
        try:
            os.mkdir(output)
        except OSError:
            print("Creation of the directory %s failed" % output)
        else:
            print("Successfully created the directory %s " % output)