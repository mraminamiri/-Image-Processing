import numpy as np
import cv2 as cv
#how we can made a black and white pic?? its simple with open cv
img = cv.imread('Crash1.jpg',0)
# 0 ====>black and white
#1 =====> Color
cv.imshow('Image',img)
cv.waitKey(0)
# BGR base
cv.destroyAllWindows()
# we want save a black and white picture
cv.imwrite('black_and_white.png',img)