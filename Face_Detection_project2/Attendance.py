import cv2
import numpy as np
import face_recognition
from datetime import datetime

import os

path = 'Attendance'
images = []
classNames = []

myList = os.listdir(path)
print(myList)

for cl in myList:
    curimg = cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)    

def findEncodng(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendnce(name):
    with open('Attendnce.csv','r+') as f:
        myDatalist = f.readline()
        namelist =[]
        for line in myDatalist:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')    


           




encodeListknown = findEncodng(images)
print('encoding complete')        


cap = cv2.VideoCapture(0)

while True:
    succes,img = cap.read()
    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

    facecurfram = face_recognition.face_locations(imgs)
    encode = face_recognition.face_encodings(imgs,facecurfram)


    for encodeFace,faceLoc in zip(encode,facecurfram):
        matches = face_recognition.compare_faces(encodeListknown,encodeFace)
        facedis = face_recognition.face_distance(encodeListknown,encodeFace)
        #print(facedis)
        matchindex = np.argmin(facedis)


        if matches[matchindex]:
            name = classNames[matchindex].upper()
           # print(name)
            y1,x2,y2,x1 = faceLoc
            y1,x2,y2,x1 =  y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendnce(name)





        cv2.imshow('webcam',img)
        #cv2.waitKey(0)   
        if cv2.waitKey(1) & 0xFF==ord('q') :
            break
        cv2.destroyAllWindows()
   cam.release()
        
        

            





