import cv2
import Filesystem
import log


def filter(filename, value, input_path, output_path):
    """ took an image and apply a blur filter on it, then save it in the output folder

    :param filename: the name of the file we want to modify
    :param value: the value of the effect we want to apply
    :param input_path: the path of the file we want to modify
    :param output_path: the path of the folder were we'll save the modified file
    """
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist:
        filter_name = 'Blur'
        if value != 0:
            try:
                image = cv2.imread(output_path + filename)
                blurImg = cv2.GaussianBlur(image, (value, value), 0)
                cv2.imwrite(output_path + filename, blurImg)
                log.filter_success(filename, filter_name)
            except cv2.error:
                pass
        else:
            log.filter_error(filter_name, filename)
    else:
        print("Your file was not found")
