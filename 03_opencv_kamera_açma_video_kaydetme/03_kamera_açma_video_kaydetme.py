import cv2

# capture
# default kamera için 0
cap = cv2.VideoCapture(0)

# çerçeve genişliği ve yüksekliği alma
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

# kamera akışını bir video dosyasına kaydetmek
# (video_adı, Four Character Code = *"DIVX", 20 = fps,  videonun boyutları kameranın çözünürlüğüne uygun olur.  )
writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20,(width,height))

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # görüntüyü yatay eksende çevirmeyi sağlar
    cv2.imshow("Video", frame)
    
    # save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xff == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()