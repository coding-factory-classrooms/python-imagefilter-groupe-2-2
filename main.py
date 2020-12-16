import cv2
import greyfilter
import blurFilter
import dilateFilter
import erodeFilter
import numpy as np




greyfilter.filter('arouf.jpg')
blurFilter.filter('arouf.jpg')
dilateFilter.filter('arouf.jpg')
erodeFilter.filter('arouf.jpg')




#
# try:
#     image = cv2.imread('assets/imgs/arouf.jpg')
#     grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     blurImg = cv2.GaussianBlur(image, (11, 11), 0)
#     cv2.imwrite('assets/output/grayArouf.jpg', grayImg)
#
#     cv2.imwrite('assets/output/blurredArouf.jpg', blurImg)
#
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# except cv2.error as e:
#     print(e)




