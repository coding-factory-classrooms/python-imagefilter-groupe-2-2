import cv2
import Filesystem
import log


def show_the_team(filename, output_path):
    new_file = "new_" + filename
    filter_name = 'ZeTeam'
    fileExist = Filesystem.isFileValid(output_path + new_file)
    if fileExist:
        try:
            image = cv2.imread(output_path + new_file)
            window_name = 'Image'
            font = cv2.FONT_HERSHEY_SIMPLEX
            org = (15, 50)
            fontScale = 2
            color = (255, 0, 0)
            thickness = 2
            image = cv2.putText(image, "Robin Yanis Killian les boss", org, font, fontScale, color, thickness, cv2.LINE_AA)
            cv2.imwrite(output_path + new_file, image)
            log.filter_success(filename, filter_name)
        except Exception as e:
            print(e)