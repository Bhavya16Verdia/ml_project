#!/usr/bin/python

import cv2

#function to find image difference. We are taking 3 frames
def diff(x,y,z):
	img1=cv2.absdiff(x,y)
	img2=cv2.absdiff(y,z)
	com_diff=cv2.bitwise_and(img1,img2)
	return com_diff

#taking 3 consistent frames
cap=cv2.VideoCapture(0)
frame1=cap.read()[1]
frame2=cap.read()[1]
frame3=cap.read()[1]

#converting into gray scale
gray1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(frame3,cv2.COLOR_BGR2GRAY)

while cap.isOpened():
	#passing arguement to above function
	img_diff=diff(gray1,gray2,gray3)
	#showing difference
	cv2.imshow('diff img',img_diff)

	#capturing new frames
	status,frame=cap.read()
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()

