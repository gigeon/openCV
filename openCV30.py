#윤곽선 검출
import cv2

img = cv2.imread('cards.png')

target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

#con, hie = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #외각선만 찾음
#con, hie = cv2.findContours(otsu, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #모든 윤곽선 찾음 (계층 정보 x)
con, hie = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) #모든 윤곽선 찾음 (계층 정보 트리구조로 o)
#윤곽선 정보, 구조
#이미지, 윤곽선 찾는 모드, 찾을때 사용할 근사치방법 : CHAIN_APPOROX_NONE(모든 좌표), CHAIN_APPROX_SIMPLE(4개의 꼭짓점만)

color = (0,200,0)
cv2.drawContours(target_img, con, -1, color, thickness=2)
#대상이미지, 윤곽선정보, -1(전체), 색, 두께

print(hie)
print(f'발견 횟수 : {len(con)}')
cv2.imshow('target',target_img)
cv2.imshow('otsu',otsu)
cv2.imshow('gray',gray)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()