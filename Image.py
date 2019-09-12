import cv2
import numpy as np
import os
import time
import json
import dropbox
import datetime
import base64
from Adafruit_IO import Client, Feed, RequestError

ADAFRUIT_IO_KEY = '****************************'
ADAFRUIT_IO_USERNAME = '**********'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')
vcap = cv2.VideoCapture("rtsp://username:password@ipaddress/Streaming/channels/101")
ct =0
dbx = dropbox.Dropbox('-************************************')
dbx.users_get_current_account()
picam_feed = aio.feeds('image')
aio.send("status",1)


while(1):
    ct += 1
    ret = vcap.grab()
    
    if ct % 20 == 0:
       ret,frame = vcap.retrieve()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray, 1.3, 5,)
     
       
       for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
         status1 = "detected"
         aio.send("face",status1)
         aio.send_data("face",status1)
         status = cv2.imwrite("/home/pi/drop/1.jpg",frame)
         status1 = cv2.imwrite("/home/pi/drop/2.jpg",frame[y:y+h, x:x+w])
         with open("/home/pi/drop/1.jpg", "rb") as imageFile:
                dbx.files_upload(imageFile.read(), "/cam01/"+str(datetime.datetime.now())+".jpg", mute = True)


         with open("/home/pi/drop/2.jpg", "rb") as b:
                image = base64.b64encode(b.read())
                image_string = image.decode("utf-8")
                aio.send_data("image", image_string)
                aio.send("status",1)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

       if not ret: break
       time.sleep(0.2)
       

       cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       aio.send("status",0)
       break

vcap.release()
cv2.destroyAllWindows()
