import cv2
import numpy as np

point = []
color=(255,0,255)
thickness = 3
drawing = False

img = cv2.imread('poker.jpg')

def show_result() :
    
    width, height = 530,710
    src = np.float32(point)
    dst = np.array([[0,0],[width,0],[width,height],[0,height]], dtype=np.float32)
    mat = cv2.getPerspectiveTransform(src,dst) 
    res = cv2.warpPerspective(img, mat, (width,height))
    cv2.imshow('res',res)


def mouse_handler(event, x, y, flags, param):
    global drawing
    
    if event == cv2.EVENT_LBUTTONDOWN :
        drawing = True
        point.append((x,y))
        
    if drawing :
        prev_point = None #t시작점
        for p in point :
            cv2.line(img,p, 15, color, cv2.FILLED )
            if prev_point :
                cv2.line(img, prev_point, point, color, thickness, cv2.LINE_AA)
        prev_point = point
        
    if len(point) == 4 :
        show_result()   
    
    cv2.imshow('img',img)

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()