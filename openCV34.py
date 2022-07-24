import cv2

cap = cv2.VideoCapture('city.mp4')
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

out = cv2.VideoWriter('city_output.avi', fourcc, fps*4, (height,width))
while(True):
    ret, frame = cap.read()
    if not ret :
        print("프레임 다 가져옴")
        break
    rotate = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    out.write(rotate)
    cv2.imshow('video', frame)
    
    #waitkey로 속도 조절
    #ord 키보드
    if cv2.waitKey(1)==ord('q') :
        print("사용자에 의해 종료")
        break

cap.release()
cv2.destroyAllWindows()