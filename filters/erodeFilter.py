import cv2
import Filesystem
import numpy as np

input_path = '../assets/imgs/'
output_path = 'assets/output/'


def filter(filename):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist == True:
        filtername = 'erroded_'
        try:
            image = cv2.imread(input_path + filename)
            kernel = np.ones((5, 5), np.uint8)
            erodeImg = cv2.erode(image, kernel, iterations=1)
            cv2.imwrite(output_path + filtername + filename, erodeImg)

        except cv2.error as e:
            print("Your File is not an image")
    else:
        print("Your file was not found")
