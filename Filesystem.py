import os.path
from os import path


def isFileValid(filepath):
    '''
    :param filepath: the path of a file
    :return: a boolean to know if the file exists or not
    '''
    if path.exists(filepath):
        return True

    else:
        return False
