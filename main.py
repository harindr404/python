import urllib
from PIL import image
import pytesseract
from resizeimage import resizeimage
import os
import cv2
import numpy as np
src_path="C:\Users\harindra sai tej\PycharmProjects\untitled"
img_path="C:\Users\harindra sai tej\PycharmProjects\untitled\A-wise-man-can-learn"


def get_string(img_path):
img=cv2.imread(img_path)
img=cv2.cvtColor(img, cv2,COLOR_BGR2GRAY)
kernel=np.ones((1,1), np.uint8)
img= cv2.dilate(img, kernel, iterations=1)
img= cv2.erode(img, kernel, iterations=1)

cv2.imwrite(src_path + "A-wise-man-can-learn.png", img)
img= cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.AWISEMANCANLEARN.png_BINARY, 11, 2)
cv2.imwrite(src_path+ "A-wise-man-can-learn.png.png", img)
result=pytesseract.image to string(image.open(src path +"A-wise-man-can-learn.png"))

return result


print 'Start recognition'
print get string(src path + "img.png")
