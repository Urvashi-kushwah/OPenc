import cv2 as cv

img = cv.imread('Russian_number.jpeg')
cv.imshow('Number', img)



gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Number', gray)

haar_cascade = cv.CascadeClassifier('haar_russianNumber.xml')

plates_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of Plates found = {len(plates_rect)}')

for (x,y,w,h) in plates_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Plates', img)



cv.waitKey(0)