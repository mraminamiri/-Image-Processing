import cv2 as cv
img = cv.imread('Crash2.jpg',cv.IMREAD_COLOR)
imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgsansoor = img[290:720,20:740]
img [120:550,110:830] = imgsansoor
#BGR



#cv.imshow('Original',img)
#cv.imshow('Gray',imgray)
#cv.imshow('sansoor',imgsansoor)
print(img.shape)
b,g,r = cv.split(img)
print(b,g,r)
cv.waitKey(0)