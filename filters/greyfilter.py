import cv2
import Filesystem
import log

input_path = 'assets/imgs/'
output_path = 'assets/output/'


def filter(filename):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist:
        filter_name = 'Gray'
        new_prefix = 'new_'
        try:
            image = cv2.imread(output_path + new_prefix + filename)
            grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(output_path + new_prefix + filename, grayImg)
            log.log_filter(filename, filter_name)
        except cv2.error:
            print(f"Your file={filename} is not an image")
    else:
        print("Your file was not found")