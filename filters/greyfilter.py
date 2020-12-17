import cv2
import Filesystem
import log


def filter(filename,output_path):
    """ took an image and apply a grey filter on it, then save it in the output folder

    :param filename: the name of the file we want to modify
    :param input_path: the path of the file we want to modify
    :param output_path: the path of the folder were we'll save the modified file
    """
    filter_name = 'Gray'
    new_file = "new_"+filename
    fileExist = Filesystem.isFileValid(output_path + new_file)
    if fileExist:
        try:
            image = cv2.imread(output_path + new_file)
            grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(output_path + new_file, grayImg)
            log.filter_success(filename, filter_name)
        except cv2.error:
            pass
    else:
        print("Your file was not found")