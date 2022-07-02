#이미지 프로세싱

#이미지 처리

import cv2
print(cv2.__version__)

img = cv2.imread('cat.jpg')
if(img is None):
    print("img is None")

img_color = cv2.imread('cat.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('img_color',img_color)
cv2.imshow('img_gray',img_gray)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()