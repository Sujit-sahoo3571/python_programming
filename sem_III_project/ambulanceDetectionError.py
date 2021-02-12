# capture the video and convert into frames 
# open => run = > exit (q)

from cv2 import cv2 as cv # in VScode 


# capture video  

capture = cv.VideoCapture(' C:\\Users\\DEVELOPER\\Downloads\\Video\\Video.avi ')

car_cascade = cv.CascadeClassifier('F:\\EVRSYSTEM\\AMBULANCE\\classifier\\cascadeAmbulance.xml') 
# convert into frames 

while  True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    for (x,y,w,h) in cars: 
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2) 

    cv.imshow('showing video',frame)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()

print('successfully Terminate ')

