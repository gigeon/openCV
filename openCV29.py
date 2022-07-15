import cv2
from cv2 import threshold
from numpy import empty

img = cv2.imread('snowman.png')

name = "Trackbar"
cv2.namedWindow(name)
cv2.createTrackbar('threshold1', name, 0, 255, empty)
cv2.createTrackbar('threshold2', name, 0, 255, empty)

while 1:
    threshold1 = cv2.getTrackbarPos('threshold1',name)
    threshold2 = cv2.getTrackbarPos('threshold2',name)
    
    canny = cv2.Canny(img, threshold1, threshold2)
    #대상이미지, mainVal, maxVal
    
    cv2.imshow('img',img)
    cv2.imshow(name,canny)
    
    if cv2.waitKey(1) == ord('q') :
        break

cv2.destroyAllWindows()