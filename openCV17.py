import cv2
import numpy as np

img = cv2.imread('poker.jpg')

width, height = 530,710

src = np.array([[702,143],[1133,414],[726,1007],[276,700]], dtype=np.float32)
dst = np.array([[0,0],[width,0],[width,height],[0,height]], dtype=np.float32)
#좌상, 우상, 우하, 좌하(시계방향 4지점 정의)

mat = cv2.getPerspectiveTransform(src,dst) #Matrix 얻어옴
res = cv2.warpPerspective(img, mat, (width,height)) #Matrix 대로 변환

cv2.imshow('img',img)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()