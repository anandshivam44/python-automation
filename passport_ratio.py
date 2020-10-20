import PIL
from PIL import Image
from matplotlib import cm
import numpy as np
import cv2
face_class = cv2.CascadeClassifier("haarcascade_frontalface_default_low_size.xml")
cam = cv2.VideoCapture(0)
count=0
while True:
    ret, img = cam.read()
    print(img.shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # PIL_image = Image.fromarray(np.uint8(img)).convert('RGB')
    # PIL_image = Image.fromarray(img.astype('uint8'), 'RGB')
    # filename="img"+str(count)+".jpg"
    # PIL_image.save(filename)
    
    # dim = gray.size
    # print(dim)
    # gray.save('gray_'+count+'.jpg')
    # count=count+1
    faces = face_class.detectMultiScale(gray, 1.3, 5)

    # convert=faces
    
    # PIL_image = Image.fromarray(np.uint8(convert)).convert('RGB')
    # PIL_image = Image.fromarray(convert.astype('uint8'), 'RGB')
    # filename="img"+str(count)+".jpg"
    # PIL_image.save(filename)

    for x,y,w,h in faces:
        # print("x = ",x)
        centre_x=x+(w)/2
        centre_y=y+(h)/2
        a=1
        b=1
        print("x = ",centre_x," y = ",centre_y)
        start_x=int(centre_x-1.5*(w/2))
        start_y=int(centre_y-(21*a)/(10*(a+b))*(w))
        end_x=int(centre_x+1.5*(w/2))
        end_y=int(centre_y+(21*b)/(10*(a+b))*(w))
        # mimg=cv2.rectangle(img, (x,y), (x+w, y+h), (244, 0, 0), 2)
        mimg=cv2.rectangle(img, (start_x,start_y), (end_x, end_y), (244, 0, 0), 2)

        cv2.imshow("My Face", mimg)
    
    if cv2.waitKey(10) == ord('s'):
        cv2.imwrite('img.jpg', mimg)
    
    if cv2.waitKey(10) == 13:    
        break
cam.release()
cv2.destroyAllWindows()