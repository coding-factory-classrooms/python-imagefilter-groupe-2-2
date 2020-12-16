import cv2
import numpy as np


image = cv2.imread('assets/imgs/arouf.jpg')
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(image, (11, 11), 0)

img = cv2.imread('assets/imgs/arouf.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
erodeImg = cv2.erode(img, kernel, iterations=1)
dilateImg = cv2.dilate(img, kernel, iterations=1)


cv2.imshow('Original image', image)
cv2.imshow('Gray image', grayImg)
cv2.imshow('Blurred image', blurImg)
cv2.imshow('erode image', erodeImg)
cv2.imshow('dilate image', dilateImg)


cv2.imwrite('assets/output/grayArouf.jpg', grayImg)
cv2.imwrite('assets/output/blurredArouf.jpg', blurImg)
cv2.imwrite('assets/output/erodeArouf.jpg', erodeImg)
cv2.imwrite('assets/output/dilateArouf.jpg', dilateImg)


cv2.waitKey(0)
cv2.destroyAllWindows()