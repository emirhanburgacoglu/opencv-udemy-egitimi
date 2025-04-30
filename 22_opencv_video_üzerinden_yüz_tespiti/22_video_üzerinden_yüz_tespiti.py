
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

turk_bayragi = cv2.imread("indir.png")


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if ret:
        face_rect = face_cascade.detectMultiScale(frame, minNeighbors=12)
        for (x,y,w,h) in face_rect:
            
            bayrak = cv2.resize(turk_bayragi, (w,h))
            frame[y:y+h, x:x+w] = bayrak
          
            cv2.imshow("Frame", frame)
    else: 
        print("kameradan görüntü alınamadı")
            
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()