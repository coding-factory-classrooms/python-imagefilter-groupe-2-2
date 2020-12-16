import cv2

image = cv2.imread('assets/imgs/arouf.jpg')
grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurImg = cv2.GaussianBlur(image,(11,11),0)


# cv2.imshow('Original image', image)
# cv2.imshow('Gray image', grayImg)
# cv2.imshow('Blurred image', blurImg)

cv2.imwrite('assets/output/grayArouf.jpg', grayImg)
cv2.imwrite('assets/output/blurredArouf.jpg', blurImg)

cv2.waitKey(0)
cv2.destroyAllWindows()