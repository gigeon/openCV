import cv2
from numpy import empty

img = cv2.imread('book.jpg', cv2.IMREAD_GRAYSCALE)

name = 'Trackbar'
cv2.namedWindow(name)

cv2.createTrackbar('block_size', name, 25, 100, empty) #홀수만 가능, 1보다 큰값
cv2.createTrackbar('c', name, 3, 10, empty) #일반적인 양수

while 1 :
    block_size = cv2.getTrackbarPos('block_size',name)
    c = cv2.getTrackbarPos('c',name)
    
    if block_size <= 1 :
        block_size = 3
        
    if block_size % 2 == 0 :
        block_size += 1
    
    binary = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, block_size, c)
    
    cv2.imshow(name,binary)
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()