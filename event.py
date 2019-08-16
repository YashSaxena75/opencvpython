import cv2
import numpy as np

def clickev(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        font=cv2.FONT_HERSHEY_COMPLEX
        xy=str(x) + ' , ' + str(y)
        cv2.putText(img,xy,(x,y),font,1,(0,255,255),2)
        cv2.imshow('image',img)
img=cv2.imread('lena.jpg',1)
cv2.imshow('image',img)

cv2.setMouseCallback('image',clickev)

cv2.waitKey(0)
cv2.destroyAllWindows()