#!/usr/bin/python

import cv2

#loading image
img=cv2.imread('virat.jpg')

#to display the image
cv2.imshow("virat",img)

#for a gray image
img1= cv2.imread('virat.jpg',0)

#save gray image
cv2.imwrite("bac.jpg",img1)
cv2.imshow("bac",img1)

#for a transparent image
img2= cv2.imread('virat.jpg',-1)

#save transparent image
cv2.imwrite("tsp.jpg",img2)
cv2.imshow("tsp",img2)

#to draw a line in the image
cv2.line(img,(0,0),(150,200),(40,70,150),3) 
cv2.imshow("lineimg",img)

#to draw a rectangle
cv2.rectangle(img,(50,50),(200,200),(255,25,200),5)
cv2.imshow("rectimg",img)

#to draw a circle
cv2.circle(img,(25,25),10,(255,25,0),5)
cv2.imshow("cirimg",img)

#image window holder activation
cv2.waitKey(0)

#to close all windows
cv2.destroyAllWindows


