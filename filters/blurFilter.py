import cv2
import Filesystem



input_path = '../assets/imgs/'
output_path = 'assets/output/'

def filter(filename):
    fileExist = Filesystem.isFileValid(input_path + filename)
    if fileExist == True:
        filtername = 'blurred_'
        try:
            image = cv2.imread(input_path + filename)
            blurImg = cv2.GaussianBlur(image, (11, 11), 0)
            cv2.imwrite(output_path + filtername + filename, blurImg)
        except cv2.error as e:
            print("Your File is not an image")
    else:
        print("Your file was not found")