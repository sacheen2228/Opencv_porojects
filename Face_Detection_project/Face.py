import cv2
import numpy as np

train_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#img = cv2.imread('RDJ.jpg')
#img = cv2.imread('sacheen.jpg')
wbcam =cv2.VideoCapture(0)

while True:
    read,fram =wbcam.read()



gray_img = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)


faces = train_face_data.detectMultiScale(gray_img)

for (x,y,w,h) in faces:
    cv2.rectangle(fram,(x,y), (x+w ,y+h) ,(0,255,0),3)
    #roi_gray = gray_img[y:y+h, x:x+w]
#(x,y,w,h) = faces[0]
#cv2.rectangle(img,(x,y), (x+w ,y+h) ,(0,255,0),3)   

cv2.imshow('Face_Detection_project',fram)
#cv2.imshow('Face_Detection_project',img)


k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()



#key=cv2.waitKey(1)



#webcam.release()




