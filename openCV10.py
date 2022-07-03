import cv2
import numpy as np

img = cv2.imread('cat.jpg')
dst = cv2.resize(img, (400,500)) #가로세로 크기 조정
dst2 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
#보간법(프레임 빈공간 채우기) 축소
dst3 = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
#보간법(프레임 빈공간 채우기) 확대

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.imshow('dst3',dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()