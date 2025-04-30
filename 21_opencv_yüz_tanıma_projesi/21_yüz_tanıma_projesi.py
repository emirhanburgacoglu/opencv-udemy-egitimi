
import matplotlib.pyplot as plt
import cv2

# resmi içe aktar
einstein = cv2.imread("einstein.jpg", 0)
plt.figure(), plt.imshow(einstein, cmap="gray"), plt.axis("off"), plt.title("Einstein"), plt.show()
/
# sınıflandırıcı
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

face_rect = face_cascade.detectMultiScale(einstein)

for (x,y,w,h) in face_rect:
    cv2.rectangle(einstein, (x,y), (x + w,y + h), (255,255,255), 10)
    plt.figure(), plt.imshow(einstein, cmap="gray"), plt.axis("off"), plt.title("Face Detect Einstein"), plt.show()

# barcelona
barce= cv2.imread("barcelona.jpg", 0)
plt.figure(), plt.imshow(barce, cmap="gray"), plt.axis("off"), plt.title("Barcelona"), plt.show()

face_rect = face_cascade.detectMultiScale(barce, minNeighbors=7)
for (x,y,w,h) in face_rect:
    cv2.rectangle(barce, (x,y), (x + w,y + h), (255,255,255), 10)
    plt.figure(), plt.imshow(barce, cmap="gray"), plt.axis("off"), plt.title("Face Detect Barcelona"), plt.show()
