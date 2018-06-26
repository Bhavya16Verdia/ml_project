#!/usr/bin/python

import cv2
import time

#reading image
img=cv2.imread("virat.jpg")

#checking shape
print img.shape

time.sleep(5) 

#printing data
print img

#extracting only red color
onlyred=cv2.inRange(img,(0,0,0),(40,40,255))

#display the original image
cv2.imshow('original image',img)

#display the only red image
cv2.imshow('onlyred image',onlyred)

#save the only red image
cv2.imwrite("red.jpg",onlyred)

cv2.waitKey(0)
cv2.destroyAllWindows()


