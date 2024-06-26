import cv2 as cv
import numpy as np
img = cv.imread('elephant.jpeg')

cv.imshow('Elephant', img)


gray  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

canny = cv.Canny(img, 125,175)
cv.imshow('Canny Egdes', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)


contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')



cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)