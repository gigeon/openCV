import cv2

img = cv2.imread('cat.jpg')
#print(img.shape) #390,640,3

#이미지 합성
crop = img[100:200, 300:400]
img[200:300, 400:500] = crop

#이미지 대칭
flip_hor = cv2.flip(img,1)
flip_ver = cv2.flip(img,0)
flip_both = cv2.flip(img,-1)

cv2.imshow('flip_hor',flip_hor)
cv2.imshow('flip_ver',flip_ver)
cv2.imshow('flip_both',flip_both)
cv2.imshow('img',img)
cv2.imshow('crop',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()