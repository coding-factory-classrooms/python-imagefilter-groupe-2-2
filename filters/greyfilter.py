import cv2
import Filesystem
import log


def filter(filename, input_path, output_path):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist:
        filter_name = 'Gray'
        try:
            image = cv2.imread(output_path + filename)
            grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(output_path + filename, grayImg)
            log.log_filter(filename, filter_name)
        except cv2.error:
            print(f"Your file={filename} is not an image")
    else:
        print("Your file was not found")