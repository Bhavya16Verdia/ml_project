import cv2
import random

cam=cv2.VideoCapture(0)
while cam.isOpened():
    print('camera is ready')
    status,frame=cam.read()
    bwimg=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.rectangle(frame,(200,100),(400,300),(0,0,255),2)
    cv2.putText(frame,'bhavya',(250,90),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow('capture', frame)
    if cv2.waitKey(1)& 0xFF==ord('a'):
		break	
    x=random.random()
    y=str(x)[3:6]
    cv2.imwrite('adhoc'+y+'.jpg',frame)
    print('capture')
cv2.destroyAllWindows()
cam.release()

