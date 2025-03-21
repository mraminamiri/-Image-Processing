import cv2 as cv
img = cv.imread('Crash2.jpg',cv.IMREAD_COLOR)

cv.line(img,(100,100),(200,200),(0,0,255),10)
cv.rectangle(img,(100,100),(200,200),(255,255,255),8)
cv.circle(img,(100,100),30,(0,255,255),-1)

#cv.polylines(img,[pts],)
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img,'its bad accident',(200,200),font,2,(1,1,255),5,cv.LINE_AA)

cv.imshow('Line',img)
cv.waitKey(0)

cv.destroyAllWindows()
