import cv2
import numpy as np

img = cv2.imread('book.jpg', cv2.IMREAD_GRAYSCALE)

ret, binary = cv2.threshold(img,127, 255, cv2.THRESH_BINARY)
#이진화 임계값 127기준 이상이면 255로


cv2.imshow('img', img)
cv2.imshow('binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()