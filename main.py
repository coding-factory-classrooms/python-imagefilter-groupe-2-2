import cv2
import os
from filters import dilateFilter, blurFilter, greyfilter, erodeFilter
import numpy as np


list = os.listdir('assets/imgs')

for files in list:
    print(files)
    image = cv2.imread('assets/imgs/'+files)
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurImg = cv2.GaussianBlur(image, (11, 11), 0)
    kernel = np.ones((5, 5), np.uint8)
    # erodeImg = cv2.erode(image, kernel, iterations=1)
    dilateImg = cv2.dilate(image, kernel, iterations=1)
    cv2.imwrite('assets/output/gray'+files, grayImg)
    cv2.imwrite('assets/output/blurred'+files, blurImg)
    # cv2.imwrite('assets/output/eroded'+files, erodeImg)
    cv2.imwrite('assets/output/dilated'+files, dilateImg)


greyfilter.filter('arouf.jpg')
blurFilter.filter('arouf.jpg')
dilateFilter.filter('arouf.jpg')
erodeFilter.filter('arouf.jpg')



# cv2.imshow('Original image', image)
# cv2.imshow('Gray image', grayImg)
# cv2.imshow('Blurred image', blurImg)
# cv2.imshow('erode image', erodeImg)
# cv2.imshow('dilate image', dilateImg)



