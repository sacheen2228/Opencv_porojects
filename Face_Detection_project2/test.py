import cv2
import numpy as np
import face_recognition

imgElon = face_recognition.load_image_file('imagesBasic/Elon-musk.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgtest = face_recognition.load_image_file('imagesBasic/Elon Musk_test.jpg')
imgtest = cv2.cvtColor(imgtest, cv2.COLOR_BGR2RGB)




faceLoc = face_recognition.face_locations(imgElon)[0]
encodElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon,(faceLoc[3],faceLoc[1] ,faceLoc[0],faceLoc[2]),(255,0,0),2)


faceLoctest = face_recognition.face_locations(imgtest)[0]
encodtest = face_recognition.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceLoctest[3],faceLoctest[0] ,faceLoctest[1],faceLoctest[2]),(255,0,255),2)







cv2.imshow('Elon-musk',imgElon)
cv2.imshow('Elon Musk_test',imgtest)




cv2.waitKey(0)




