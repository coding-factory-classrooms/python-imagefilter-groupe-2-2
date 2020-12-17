import cv2
import Filesystem
import numpy as np
import log


def filter(filename, value, input_path, output_path):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist:
        filter_name = 'Dilate'

        if value != 0:
            try:
                image = cv2.imread(output_path + filename)
                kernel = np.ones((value, value), np.uint8)
                dilateImg = cv2.dilate(image, kernel, iterations=1)
                cv2.imwrite(output_path + filename, dilateImg)
                log.filter_success(filename, filter_name)

            except cv2.error:
                pass
        else:
            log.filter_error(filter_name, filename)
    else:
        print("Your file was not found")
