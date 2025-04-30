import cv2
import numpy as np

# Resmi içe aktarma
img = cv2.imread("odev2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Orijinal resmi görselleştirme

# Kenar algılama
edges = cv2.Canny(gray, threshold1=200, threshold2=255)


# Haar Cascade Yüz Tespiti
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray)

img_faces = img.copy()
for (x, y, w, h) in faces:
    cv2.rectangle(img_faces, (x, y), (x + w, y + h), (255, 255, 255), 5)
cv2.imshow("Yüz Tespiti", img_faces)

# HOG İnsan Tespiti
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
(rects, weights) = hog.detectMultiScale(gray, padding=(8, 8), scale=1.05)

img_people = img.copy()
for (xH, yH, wH, hH) in rects:
    cv2.rectangle(img_faces, (xH, yH), (xH + wH, yH + hH), (0, 255, 0), 4)
    cv2.imshow("İnsan Tespiti", img_faces)
    
    if cv2.waitKey(0) & 0xFF == ord("q"):
        continue
cv2.destroyAllWindows()



