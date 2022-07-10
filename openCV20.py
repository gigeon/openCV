import cv2
import numpy as np

point = []
img = cv2.imread('poker.jpg')
img = cv2.resize(img, None, fx = 0.5, fy = 0.5)
color=(255,0,255)
thickness = 3
drawing = False

def show_result() :
    
    width, height = 530,710
    src = np.float32(point)
    dst = np.array([[0,0],[width,0],[width,height],[0,height]], dtype=np.float32)
    mat = cv2.getPerspectiveTransform(src,dst) 
    res = cv2.warpPerspective(img, mat, (width,height))
    cv2.imshow('res',res)


def mouse_handler(event, x, y, flags, param):
    global drawing
    dst_img = img.copy()
    
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 Down
        drawing = True # 선을 그리기 시작
        point.append((x, y))
     
    if drawing:
        prev_point = None # 직선의 시작점
        for p in point:
            cv2.circle(dst_img, p, 10, color, cv2.FILLED)
            if prev_point:
                cv2.line(dst_img, prev_point, p, color, thickness, cv2.LINE_AA)
            prev_point = p
        
        next_point = (x, y)
        if len(point) == 4:
            show_result() # 결과 출력
            next_point = point[0] # 첫 번째 클릭한 지점
            
        cv2.line(dst_img, prev_point, next_point, color, thickness, cv2.LINE_AA)
        
    cv2.imshow('img', dst_img)

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()