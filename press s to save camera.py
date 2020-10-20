import cv2
cam = cv2.VideoCapture(0)
count=0
while True:
    ret, img = cam.read()
    cv2.imshow("test", img)
    #press s to save
    if cv2.waitKey(10) == ord('s'):
        filename="img"+str(count)+".jpg"
        cv2.imwrite(filename, img)
        count=count+1
    # press Esc to break
    if cv2.waitKey(10) == 27:    
        break
cam.release()
cv2.destroyAllWindows()
