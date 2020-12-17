import cv2
import Filesystem
import log


def filter(filename, input_path, output_path):
    """ took an image and apply a grey filter on it, then save it in the output folder

    :param filename: the name of the file we want to modify
    :param input_path: the path of the file we want to modify
    :param output_path: the path of the folder were we'll save the modified file
    """
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