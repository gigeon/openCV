import cv2
import numpy as np
import serial
import time

arduino = serial.Serial('/dev/cu.usbmodem101',9600)
time.sleep(1)

cap = cv2.VideoCapture(0)
PINK_MIN = np.array([100,80,2], np.uint8)
PINK_MAX = np.array([126,255,255], np.uint8)

centroid_x = 0
centroid_y = 0

toggle1 = False
toggle2 = False
toggle3 = False

while(1):

    ret, img = cap.read()
    img = cv2.flip(img, 1)

    #thresh = cv2.namedWindow('Threshold', cv2.WINDOW_NORMAL)
    orig = cv2.namedWindow('Original', cv2.WINDOW_NORMAL)
    #img = cv2.GaussianBlur(img, (15, 15), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    #grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #_, frame_threshed = cv2.threshold(grey, 127, 255,
    #                        cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

    frame_threshed = cv2.inRange(hsv, PINK_MIN, PINK_MAX)

    contours,hierarchy = cv2.findContours(frame_threshed, 1, 2)
    max_area = 0
    last_x = centroid_x
    last_y = centroid_y

    if contours:
        for i in contours:
            area = cv2.contourArea(i)
            if area > max_area:
                max_area = area
                cnt = i

        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        centroid_x = int((x + x+w)/2)
        centroid_y = int((y + y+h)/2)

        cv2.circle(img, (centroid_x, centroid_y), 2, (0,0,255), 2)

        cv2.line(img,(300,0),(300,800),(0,255,0),5)
        cv2.line(img,(600,0),(600,800),(0,255,0),5)

        #cv2.imshow('Threshold', frame_threshed)
        cv2.imshow('Original', img)


 
        # up-down move
        #if centroid_x >= 196 and centroid_x <= 392:
            # up
         #   if centroid_y >= 0 and centroid_y <= 240:
          #      print ('up')
                # pyautogui.press('up')
            # down
           # if centroid_y >= 240 and centroid_y <=480:
            #    print ('down')
                # pyautogui.press('down')
        
        # left-right move
        if centroid_y >= 0 and centroid_y <= 800:
            # left
            if centroid_x >= 0 and centroid_x <= 300:
                if toggle1 == False and toggle2 == False:
                    data = '1'
                    data = data.encode('utf-8')
                    print ('left')
                    arduino.write(data)
                    toggle1 = True
                    toggle2 = True
                    toggle3 = False
                if toggle1 == True and toggle2 == False:
                    data = '1'
                    data = data.encode('utf-8')
                    print ('left')
                    arduino.write(data)
                    toggle2 = True
                    toggle3 = False
            # right
            if centroid_x >= 600:
                if toggle1 == False and toggle3 == False:
                    data = '0'
                    data = data.encode('utf-8')
                    print ('right')
                    arduino.write(data)
                    toggle1 = True
                    toggle2 = False
                    toggle3 = True
                if toggle1 == True and toggle3 == False:
                    data = '0'
                    data = data.encode('utf-8')
                    print ('right')
                    arduino.write(data)
                    toggle2 = False
                    toggle3 = True
            else :
                print('center')
                
    # k = cv2.waitKey(10)
    # if k == 27:
    #     break
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
