import cv2
import Filesystem
import log
import random

def show_the_team(filename, output_path, message):
    new_file = "new_" + filename
    filter_name = 'ZeTeam'
    fileExist = Filesystem.isFileValid(output_path + new_file)
    if fileExist:
        try:
            image = cv2.imread(output_path + new_file)
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (200, 200)
            fontScale = 2
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            thickness = 2
            image = cv2.putText(image, message, org, font, fontScale, color, thickness, cv2.LINE_AA)
            cv2.imwrite(output_path + new_file, image)
            log.filter_success(filename, filter_name)
        except Exception as e:
            print(e)