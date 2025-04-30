import cv2

path = "cascade.xml"

object_name = "Kalem Ucu"

frame_width = 280
frame_height = 360

color = (255,0,255)

cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)

def empty(val):
    pass

# trackbar
cv2.namedWindow("Sonuc")
cv2.resizeWindow("Sonuc", frame_width, frame_height + 100)
cv2.createTrackbar("Scale","Sonuc", 400, 1000, empty)
cv2.createTrackbar("Neighbor","Sonuc", 4, 50, empty)

# cascade classifier
cascade = cv2.CascadeClassifier(path)

while True:
    # read frame
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    if ret:
        # convert bgr to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # detection parametreleri
        scaleVal = 1 + (cv2.getTrackbarPos("Scale", "Sonuc")/1000)
        
        neighbor = 1 + (cv2.getTrackbarPos("Neighbor", "Sonuc"))
        
        #detection
        rects = cascade.detectMultiScale(gray, scaleVal, neighbor)
        
        for (x,y,w,h) in rects:
            cv2.rectangle(frame, (x,y),(x+w,y+h), color, 3)
            cv2.putText(frame, object_name , (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL ,1 , color, 2)
            
        cv2.imshow("Sonuc", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
            
        
        
        