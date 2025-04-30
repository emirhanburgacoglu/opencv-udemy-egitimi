import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
if not ret:
    print("Kamera açılamadı.")
    cap.release()
    cv2.destroyAllWindows()
    exit()

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
face_rect = face_cascade.detectMultiScale(
    gray_frame, scaleFactor=1.045, minNeighbors=5, minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE
)

if len(face_rect) == 0:
    print("Yüz bulunamadı.")
    cap.release()
    cv2.destroyAllWindows()
    exit()

(face_x, face_y, w, h) = tuple(face_rect[0])
track_window = (face_x, face_y, w, h)

roi = frame[face_y: face_y + h, face_x: face_x + w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0, 1], roi_hist, [0, 180, 0, 256], 1)

    ret, track_window = cv2.CamShift(dst, track_window, term_crit)
    pts = cv2.boxPoints(ret)
    pts = np.int0(pts)
    img2 = cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

    cv2.imshow("Takip", img2)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
