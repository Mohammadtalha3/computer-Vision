from lib2to3.pytree import convert
import cv2 as cv
import numpy as np

img= cv.imread("D:\opencv/recourses\image.jpg")
img= cv.resize(img, (800,600))





gray_img=cv.cvtColor (img, cv.COLOR_BGR2GRAY)


cv.imshow("original", img)
cv.waitKey(0)
cv.destroyAllWindows()