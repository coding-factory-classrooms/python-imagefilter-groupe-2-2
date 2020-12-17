import cv2
import Filesystem

input_path = 'assets/imgs/'
output_path = 'assets/output/'

def filter(filename):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist == True:
        filtername = 'new_'
        try:
            image = cv2.imread(output_path + "new_" + filename)
            grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(output_path + filtername + filename, grayImg)
        except cv2.error:
            print(f"Your file={filename} is not an image")
    else:
        print("Your file was not found")