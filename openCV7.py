import cv2
import numpy as np

#한글 우회
from PIL import ImageFont, Image, ImageDraw

def myPutText(src, text, pos, font_size, font_color) :
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font= font, fill = font_color)
    return np.array(img_pil)

img = np.zeros((480,640,3), dtype= np.uint8)

color = (255,255,255)
thickness = 1
scale = 1

font_size = 30

#cv2.putText(img, "Nado Simplex", (20,150), cv2.FONT_HERSHEY_PLAIN, scale, color, thickness)
#cv2.putText(img, "Nado Simplex", (20,250), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, scale, color, thickness)
#cv2.putText(img, "Nado Simplex", (20,350), cv2.FONT_HERSHEY_TRIPLEX, scale, color, thickness)
#cv2.putText(img, "Nado Simplex", (20,450), cv2.FONT_ITALIC, scale, color, thickness)
#그릴위치, 텍스트내용, 시작위치, 폰트종류, 크기, 색깔, 두께
#cv2.putText(img, "ㅎㅇ", (20,50), cv2.FONT_HERSHEY_SIMPLEX, scale, color, thickness)
img = myPutText(img, "비프로 가자", (20,50), font_size,color)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
