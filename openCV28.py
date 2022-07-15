#닫힘 팽창후 침식, 구멍을 메운 후 다시 깍음
import cv2
import numpy as np

kernel = np.ones((3,3), dtype=np.uint8)

img = cv2.imread('images.png',cv2.IMREAD_GRAYSCALE)

dilate = cv2.dilate(img, kernel, iterations=3)
erode = cv2.erode(dilate, kernel, iterations=3)

cv2.imshow('img',img)
cv2.imshow('eorde',erode)
cv2.imshow('dilate',dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()