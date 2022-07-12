import cv2
from numpy import empty

img = cv2.imread('book.jpg', cv2.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('threshold', name, 127, 255, empty) #바 이름, 창 이름, 초기값, 최대값, 이벤트처리

while 1 :
    thresh = cv2.getTrackbarPos('threshold',name) #바 이름 , 창의 이름
    ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY) 
    
    if not ret:
        break
    
    cv2.imshow(name,binary)
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()
