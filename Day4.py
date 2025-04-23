import cv2 as cv
import numpy as np
img = cv.imread('ff.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # تبدیل به grayscale
ret , thresh = cv.threshold(img, 10, 255, cv.THRESH_BINARY)
#outso threshodling just one threshold
ret2,thresh2 = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
#adaptive threshold many thresholds were choised
tresh3 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,115,1)
cv.imshow('threshold3', tresh3)
cv.imshow('threshold2', thresh2)
cv.imshow('thresh', thresh)
cv.waitKey(0)
