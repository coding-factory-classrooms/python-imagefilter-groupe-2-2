import cv2
import Filesystem
import numpy as np

input_path = 'assets/imgs/'
output_path = 'assets/output/'


def filter(filename, value):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist == True:
        filtername = 'Dilate'
        new_prefix = 'new_'
        if value != 0:
            try:
                image = cv2.imread(output_path+"new_" + filename)
                kernel = np.ones((value, value), np.uint8)
                dilateImg = cv2.dilate(image, kernel, iterations=1)
                cv2.imwrite(output_path + new_prefix + filename, dilateImg)

            except cv2.error:
                print(f"Your file={filename} is not an image")
        else:
            print("Your input value was not referenced so, cannot apply dilate filter")

    else:
        print("Your file was not found")
