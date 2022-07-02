import cv2
from cv2 import LINE_AA
import numpy as np

img = np.zeros((480,640,3), dtype=np.uint8)

color_line = (0,255,255)
color_cir = (255,255,0)
color_rec = (255,0,255)
color_n = (122,3,204)
thickness = 3
radius = 50
cv2.line(img, (50,100),(400,50),color_line,thickness,cv2.LINE_8)
#그릴위치, 시작점, 끝점, 색깔, 두께, 선종류

cv2.circle(img, (200,100), radius, color_cir, thickness=10) #속이 빈 원
#그릴위치, 중심점, 반지름, 색, 두께
cv2.circle(img, (400,100), radius, color_cir, cv2.FILLED) #속이 찬 원

cv2.rectangle(img, (100,100),(200,200),color_rec, thickness=3)
cv2.rectangle(img, (300,100),(400,300),color_rec, cv2.FILLED)
#사각형

pts1 = np.array([[100,100],[200,100],[100,200]])
pts2 = np.array([[200,100],[300,100],[300,200]])

cv2.polylines(img, [pts1], False, color_n, cv2.LINE_AA)
cv2.polylines(img, [pts2], False, color_n, cv2.LINE_AA)

cv2.polylines(img, [pts1,pts2], True, color_n, thickness, cv2.LINE_AA)
#그릴 위치, 그릴 좌표, 선 닫힘 여부, 색, 두께, 선종류

pts3 = np.array([[[100,300],[200,300],[100,400]], [[200,300],[300,300],[300,400]]])

cv2.fillPoly(img,pts3, color_n, cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()