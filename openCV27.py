import cv2
# 열림 : 침식 후 팽창, 깍아서 노이즈 제거 후 살찌움
import cv2
import numpy as np
kernel = np.ones((3,3), dtype=np.uint8)

img = cv2.imread('images.png',cv2.IMREAD_GRAYSCALE)

erode = cv2.erode(img, kernel, iterations=3)
dilate = cv2.dilate(erode, kernel, iterations=3)


cv2.imshow('img',img)
cv2.imshow('eorde',erode)
cv2.imshow('dilate',dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()