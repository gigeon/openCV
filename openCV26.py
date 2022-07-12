import cv2
from cv2 import erode
import numpy as np

kernel = np.ones((3,3), dtype=np.uint8)

img = cv2.imread('images.png', cv2.IMREAD_GRAYSCALE)

erode1 = cv2.erode(img, kernel, iterations=1)
erode2 = cv2.erode(img, kernel, iterations=2)
erode3 = cv2.erode(img, kernel, iterations=3)

cv2.imshow('img',img)
cv2.imshow('1',erode1)
cv2.imshow('2',erode2)
cv2.imshow('3',erode3)
cv2.waitKey(0)
cv2.destroyAllWindows()