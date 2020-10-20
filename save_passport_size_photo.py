#press S to save photo
# press Esc continously to exit 
import PIL
from PIL import Image
from matplotlib import cm
import numpy as np
import cv2
face_class = cv2.CascadeClassifier("haarcascade_frontalface_default_low_size.xml")
cam = cv2.VideoCapture(0)
count=0
a=1
b=1
sum=a+b
count=0
while True:
    ret, img = cam.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_class.detectMultiScale(gray, 1.3, 5)
    for x,y,w,h in faces:
        centre_x=x+(w/2)
        centre_y=y+(h/2)
        start_x=int(centre_x-1.5*(w/2))
        start_y=int(centre_y-(21*a)/(10*(sum))*(w))
        end_x=int(centre_x+1.5*(w/2))
        end_y=int(centre_y+(21*b)/(10*(sum))*(w))
        # crop_img = img[start_y:end_y, start_x:end_x]
        # mimg=cv2.rectangle(img, (x,y), (x+w, y+h), (244, 0, 0), 2)
        mimg=cv2.rectangle(img, (start_x-5,start_y-5), (end_x+5, end_y+5), (244, 0, 0), 2)

        cv2.imshow("My Face", mimg)
        if cv2.waitKey(10) == ord('s'):
            crop_img = img[start_y:end_y, start_x:end_x]
            filename="img_"+str(count)+".jpg"
            cv2.imwrite(filename, crop_img)
            count=count+1
            # cv2.imwrite('img.jpg', img)
    
    
    
    if cv2.waitKey(10) == 27:#press Esc to exit programe    
        break
cam.release()
cv2.destroyAllWindows()