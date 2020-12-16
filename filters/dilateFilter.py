import cv2
import Filesystem
import numpy as np

input_path = 'assets/imgs/'
output_path = 'assets/output/'


def filter(filename, value):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist == True:
        filtername = 'dilated_'
        if value != 0:
            try:
                image = cv2.imread(input_path + filename)
                kernel = np.ones((value, value), np.uint8)
                dilateImg = cv2.dilate(image, kernel, iterations=0)
                cv2.imwrite(output_path + filtername + filename, dilateImg)

            except cv2.error:
                print(f"Your file={filename} is not an image")
        else:
            print("Your input value was not referenced so, cannot apply dilate filter")

    else:
        print("Your file was not found")
