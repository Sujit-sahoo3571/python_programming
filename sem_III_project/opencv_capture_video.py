# capture the video and convert into frames 
# open => run = > exit (q)

from cv2 import cv2 as cv # in VScode 


# capture video  

capture = cv.VideoCapture(0)

# convert into frames 

while  True:
    isTrue, frame = capture.read()
    cv.imshow('showing video',frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

print('successfully Terminate ')

