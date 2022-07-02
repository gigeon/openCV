import cv2
import numpy as np

#가로 세로 channel 만들기
img = np.zeros((480,640,3), dtype=np.uint8)
#img[:] = (255,255,255) #전체공간 흰색으로 채우기
#print(img)

#가로세로 원하는 구역에 색 채우기
img[100:200,200:300] = (255,255,255)
print(img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()