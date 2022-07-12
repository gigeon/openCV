from attr import asdict


import cv2
import numpy as np

kernel = np.ones((3,3), dtype=np.uint8)

img = cv2.imread('img.png', cv2.IMREAD_GRAYSCALE)

dilate1 = cv2.dilate(img, kernel, iterations=1) #반복횟수
dilate2 = cv2.dilate(img, kernel, iterations=2) #반복횟수
dilate3 = cv2.dilate(img, kernel, iterations=3) #반복횟수

cv2.imshow('img',img)
cv2.imshow('1',dilate1)
cv2.imshow('2',dilate2)
cv2.imshow('3',dilate3)
cv2.waitKey(0)
cv2.destroyAllWindows()