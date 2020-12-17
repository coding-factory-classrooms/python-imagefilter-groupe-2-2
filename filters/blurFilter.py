import cv2
import Filesystem
import log


def filter(filename, value, input_path, output_path):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist:
        filter_name = 'Blur'
        if value != 0:
            try:
                image = cv2.imread(output_path + filename)
                blurImg = cv2.GaussianBlur(image, (value, value), 0)
                cv2.imwrite(output_path + filename, blurImg)
                log.log_filter(filename, filter_name)
            except cv2.error:
                print(f"Your file={filename} is not an image")
        else:
            log.log_error(filter_name, filename)
    else:
        print("Your file was not found")
