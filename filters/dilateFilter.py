import cv2
import Filesystem
import numpy as np
import log


def filter(filename, value,output_path):
    """ took an image and dilate it, then save it in the output folder

       :param filename: the name of the file we want to modify
       :param value: the value of the effect we want to apply
       :param input_path: the path of the file we want to modify
       :param output_path: the path of the folder were we'll save the modified file
       """
    new_file = "new_"+filename
    filter_name = 'Dilate'
    fileExist = Filesystem.isFileValid(output_path + new_file)
    if fileExist:

        if value != 0:
            try:
                image = cv2.imread(output_path + new_file)
                kernel = np.ones((value, value), np.uint8)
                dilateImg = cv2.dilate(image, kernel, iterations=1)
                cv2.imwrite(output_path + new_file, dilateImg)
                log.filter_success(filename, filter_name)

            except cv2.error:
                pass
        else:
            log.filter_error(filter_name, filename)
    else:
        print("Your file was not found")
