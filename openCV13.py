import cv2

img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)

rotate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotate_270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('img',img)
cv2.imshow('rotate_90',rotate_90)
cv2.imshow('rotate_270',rotate_270)
cv2.waitKey(0)
cv2.destroyAllWindows()