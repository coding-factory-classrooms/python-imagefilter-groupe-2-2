import cv2
import os
from filters import dilateFilter, blurFilter, greyfilter, erodeFilter
import numpy as np


list = os.listdir('assets/imgs')

for files in list:
    print(files)
    greyfilter.filter(files)
    blurFilter.filter(files)
    dilateFilter.filter(files)
    # erodeFilter.filter(files)



# cv2.imshow('Original image', image)
# cv2.imshow('Gray image', grayImg)
# cv2.imshow('Blurred image', blurImg)
# cv2.imshow('erode image', erodeImg)
# cv2.imshow('dilate image', dilateImg)



