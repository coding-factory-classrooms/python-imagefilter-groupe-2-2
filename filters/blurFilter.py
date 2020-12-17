import cv2
import Filesystem
import log

input_path = 'assets/imgs/'
output_path = 'assets/output/'


def filter(filename, value):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist:
        filter_name = 'Blur'
        new_prefix = 'new_'
        if value != 0:
            try:
                image = cv2.imread(output_path+new_prefix + filename)
                blurImg = cv2.GaussianBlur(image, (value, value), 0)
                cv2.imwrite(output_path + new_prefix + filename, blurImg)
                log.filter_success(filename, filter_name)
            except cv2.error:
                pass
        else:
            log.filter_error(filter_name, filename)
    else:
        print("Your file was not found")
