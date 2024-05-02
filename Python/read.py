'''print("hii")

if 1>2:
    print ("yess")
else :
    print ("noo") '''


###Reading Images
import cv2 as cv

img = cv.imread('flower.jpeg')

cv.imshow('urvi', img)

cv.waitKey(0)

###Reading Videos

'''import cv2 as cv

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()'''
