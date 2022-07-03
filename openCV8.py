import cv2
import numpy as np

#이미지 저장
img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('img', img)
cv2.waitKey(0)
result = cv2.imwrite('img_save.jpg', img)
print(result)

#동영상 저장

#코덱정의
fource = cv2.VideoWriter_fourcc(*'DIVX')

cap = cv2.VideoCapture('cap.mp4')


while True:
    ret, frame = cap.read()
    
    if not ret :
        break

    cv2.imshow('video', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()