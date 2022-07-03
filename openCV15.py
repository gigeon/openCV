import cv2

img = cv2.imread('cat.jpg')

#가우시안 블러
kernel_3 = cv2.GaussianBlur(img, (3,3),0)
kernel_5 = cv2.GaussianBlur(img, (5,5),0)
kernel_7 = cv2.GaussianBlur(img, (7,7),0)
sigma_3 = cv2.GaussianBlur(img, (3,3),1)
sigma_5 = cv2.GaussianBlur(img, (5,5),2)
sigma_7 = cv2.GaussianBlur(img, (7,7),3)


cv2.imshow('img',img)
cv2.imshow('kernel3',kernel_3)
cv2.imshow('kernel5',kernel_5)
cv2.imshow('kernel7',kernel_7)
cv2.imshow('sigma7',sigma_7)
cv2.imshow('sigma5',sigma_5)
cv2.imshow('sigma3',sigma_3)
cv2.waitKey(0)
cv2.destroyAllWindows