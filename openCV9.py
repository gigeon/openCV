import cv2

#비디오 형식
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

cap = cv2.VideoCapture('cat.mp4')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#재생속도
fps = int(cap.get(cv2.CAP_PROP_FPS))

#저장 파일명
out = cv2.VideoWriter('output.mp4',fourcc,fps,(width, height))

while(True):
    ret, frame = cap.read()
    if not ret :
        break
    
    out.write(frame)
    cv2.imshow('video', frame)
    
    if cv2.waitKey(1)==ord('q') :
        break
    
out.release() #자원해제
cap.release()
cv2.destroyAllWindows()

