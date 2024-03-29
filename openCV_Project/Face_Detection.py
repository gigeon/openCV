import cv2
from cv2 import KeyPoint
import mediapipe as mp

#에러남
def overlay(image, x,y,w,h,overlay_image) : #대상이미지, x, y, w, h, 덮어씌울 이미지
    alpha = overlay_image[:, :, 3] #BGRA
    mask_image = alpha / 255 #0~1사이값
    
    for i in range(0,3) :
        image[y-h:y+h,x-w:x+w,i] = (overlay_image[:,:,i] * mask_image) + (image[y-h : y+h, x-w:x+w,i] * (1-mask_image))  


#얼굴 찾고, 표시해주는 변수정의
mp_face_detection = mp.solutions.face_detection #얼굴 검출위한 모듈
mp_drawing = mp.solutions.drawing_utils #얼굴의 특징을 그리기위한 모듈

#파일 불러오기
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('face.mp4')
img_left_eye = cv2.imread('left_eye.png') #100x100
img_right_eye = cv2.imread('right_eye.png') #100x100
img_nose = cv2.imread('nose.png') #300x100

#model_selection 0이면 근거리 1이면 장거리
#min_detection_confidence 70%이상일시 얼굴로 표시
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.7) as face_detection:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

    #성능 향상 
    # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image)

    # Draw the face detection annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)
                #print(detection)
                
                Keypoints = detection.location_data.relative_keypoints
                right_eye = Keypoints[0]
                left_eye = Keypoints[1]
                nose = Keypoints[2]
                
                h, w, ch = image.shape #height, width, channel
                right_eye = (int(right_eye.x*w)-20, int(right_eye.y*h)-100)
                left_eye = (int(left_eye.x*w)+20, int(left_eye.y*h)-100)
                nose = (int(nose.x*w), int(nose.y*h))
                
                #눈 코에 원 그리기
                #cv2.circle(image, right_eye, 50, (255,0,0), 10, cv2.LINE_AA)
                #cv2.circle(image, left_eye, 50, (0,255,0), 10, cv2.LINE_AA)
                #cv2.circle(image, nose, 50, (0,0,255), 20, cv2.LINE_AA)
                
                #이미지 그리기
                image[right_eye[1] - 50:right_eye[1]+50,right_eye[0] - 50:right_eye[0]+50] = img_right_eye
                image[left_eye[1] - 50:left_eye[1]+50,left_eye[0] - 50:left_eye[0]+50] = img_left_eye
                image[nose[1] - 50:nose[1]+50, nose[0] - 150 : nose[0] + 150] = img_nose
                
                #overlay(image, *right_eye, 50, 50, img_right_eye)
                #overlay(image, *left_eye, 50, 50, img_left_eye)
                #overlay(image, *nose, 50, 50, img_nose)
                
                
    # Flip the image horizontally for a selfie-view display. 
        cv2.imshow('MediaPipe Face Detection', cv2.resize(image, None, fx=0.5,fy=0.5))
        #cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
        if cv2.waitKey(1) == ord('q'):
            break
  
cap.release()
cv2.destroyAllWindows()