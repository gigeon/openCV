import cv2

img = cv2.imread('cards.png')

target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
con, hie = cv2.findContours(otsu, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)


color = (0,200,0)

for cnt in con :
    if cv2.contourArea(cnt) > 25000:
        x,y,width,height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x,y), (x+width,y+height),color,2)

print(hie)
print(f'발견 횟수 : {len(con)}')
cv2.imshow('target',target_img)
cv2.imshow('otsu',otsu)
cv2.imshow('gray',gray)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()