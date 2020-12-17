import os
from os import path
import log


def create_directory(output):
    if not path.exists(output):
        try:
            os.mkdir(output)
        except OSError:
            log.directory_failed(output)
        else:
            log.directory_created(output)