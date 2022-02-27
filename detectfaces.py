import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("oscar.mp4")


face_locations = []

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05,
        minNeighbors=20,
        minSize=(30, 30),)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

        cv2.imshow('Oscar', frame)

        if cv2.waitKey(3) & 0xFF == ord("q"):
            break

video.release()
cv2.destroyAllWindows()

    

