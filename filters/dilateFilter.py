import cv2
import Filesystem
import numpy as np
import log

input_path = 'assets/imgs/'
output_path = 'assets/output/'


def filter(filename, value):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist:
        filter_name = 'Dilate'
        new_prefix = 'new_'
        if value != 0:
            try:
                image = cv2.imread(output_path+new_prefix+ filename)
                kernel = np.ones((value, value), np.uint8)
                dilateImg = cv2.dilate(image, kernel, iterations=1)
                cv2.imwrite(output_path + new_prefix + filename, dilateImg)
                log.log_filter(filename, filter_name)

            except cv2.error:
                print(f"Your file={filename} is not an image")
        else:
            log.log_error(filter_name, filename)
    else:
        print("Your file was not found")
