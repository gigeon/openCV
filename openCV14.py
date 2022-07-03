import cv2

img = cv2.imread('cat.jpg')

dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img',img)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()