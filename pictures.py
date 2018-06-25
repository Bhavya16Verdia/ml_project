#!/usr/bin/python

import cv2

#loading image
img=cv2.imread('virat.jpeg')

#print height and weight
print img.shape

#to display the image
cv2.imshow("virat",img)

#image window holder activation
cv2.waitKey(0)

#to close all windows
cv2.destroyAllWindows

#to remove color from the image
img1=cv2.imread('virat.jpeg',0)

