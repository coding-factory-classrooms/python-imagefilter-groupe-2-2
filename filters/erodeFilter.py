import cv2
import Filesystem
import numpy as np
import log

input_path = 'assets/imgs/'
output_path = 'assets/output/'


def filter(filename):
    file_exist = Filesystem.isFileValid(input_path + filename)
    if file_exist:
        filter_name = 'erroded_'
        try:
            image = cv2.imread(input_path + filename)
            kernel = np.ones((5, 5), np.uint8)
            erode_img = cv2.erode(image, kernel, iterations=1)
            cv2.imwrite(output_path + filter_name + filename, erode_img)
            log.log_filter(filename, filter_name)
        except cv2.error as e:
            print("Your File is not an image")
    else:
        print("Your file was not found")
