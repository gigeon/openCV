import cv2

cap = cv2.VideoCapture('cat.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_resized = cv2.resize(frame, None, fx=1.5,fy=1.5, interpolation=cv2.INTER_CUBIC)
    
    cv2.imshow('video_resize',frame_resized)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) == ord('q') :
        break
    
cap.release()
cv2.destroyAllWindows()