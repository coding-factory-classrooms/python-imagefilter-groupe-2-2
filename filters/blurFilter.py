import cv2
import Filesystem



input_path = 'assets/imgs/'
output_path = 'assets/output/'

def filter(filename, value):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist == True:
        filtername = 'blurred_'
        if value != 0:
            try:
                image = cv2.imread(input_path + filename)
                blurImg = cv2.GaussianBlur(image, (value, value), 0)
                cv2.imwrite(output_path + filtername + filename, blurImg)
            except cv2.error:
                print(f"Your file={filename} is not an image")
        else:
            print(f"Your input value was not referenced so, cannot apply blur filter")
    else:
        print("Your file was not found")