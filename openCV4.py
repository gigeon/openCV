import cv2

cap = cv2.VideoCapture(0) #0번째 카메라 장치

while 1 :
    ret, frame = cap.read()
    
    if not ret :
        break
    cv2.imshow('camera',frame)
    if cv2.waitKey(1) == ord('q') :
        break
    
cap.release()
cv2.destroyAllWindows()