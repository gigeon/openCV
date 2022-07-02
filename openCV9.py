import cv2

fource = cv2.VideoWriter_fourcc(*'DIVX')

cap = cv2.VideoCapture('cat.mp4')


while(True):
    ret, frame = cap.read()
    if not ret :
        print("프레임 다 가져옴")
        break
    cv2.imshow('video', frame)
    
    #waitkey로 속도 조절
    #ord 키보드키
    if cv2.waitKey(25)==ord('q') :
        print("사용자에 의해 종료")
        break

cap.release()
cv2.destroyAllWindows()

