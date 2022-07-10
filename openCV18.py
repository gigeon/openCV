import cv2
from cv2 import EVENT_RBUTTONDOWN
import numpy as np

def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN :#마우스 왼쪽 버튼 누름
        print("Left Down")
        print(x,y)
    elif event == cv2.EVENT_RBUTTONDOWN : #마우스 우측 보튼 누름
        print("Right Down")
        print(x,y)
    elif event == cv2.EVENT_LBUTTONDBLCLK :
        print("Left Double Click")
    elif event == cv2.EVENT_MOUSEMOVE :
        print("Mouse Move")
    elif event == cv2.EVENT_LBUTTONUP :
        print("Left Up")
    
    
img = cv2.imread('poker.jpg')

cv2.namedWindow('img')
#img란 윈도우 이름 먼저 만들기 (마우스 이벤트 처리 위해)

cv2.setMouseCallback('img', mouse_handler)

cv2.waitKey(0)
cv2.destroyAllWindows()