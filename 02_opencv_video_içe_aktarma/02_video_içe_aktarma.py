import cv2
import time

# video ismi
video_name = "MOT17-04-DPM.mp4"

# video içe aktar: capture, cap

cap = cv2.VideoCapture(video_name) # cv2 kütüphanesini kullanarak cap nesnesi oluşturur

print("Genişlik: ", cap.get(3)) # cap.get(3) 3 parametresi genişlik döner 
print("Yükseklik: ", cap.get(4)) # cap.get(4) 4 parametresi yükseklik döner 

if cap.isOpened() == False: # cap nesnesinin açılabilip açılamayacağını döner 
    print("Hata") # açılmazsa hata mesajı alırız

while True:  
    ret, frame = cap.read() # video nesnesi okunur ve return, frame döner
    
    if ret == True: # görüntülere ulaşabildiysek true
        time.sleep(0.01) # yavaşlatma
        cv2.imshow("Video", frame) # pencerecede frameleri görüntülememizi sağlar
    else: break # görüntü biterse çıkmamızı sağlar

    if cv2.waitKey(1) & 0xFF == ord("q"): # q harfi çıkış yapmamamızı saplar
        break
    
    
cap.release() # stop capture
cv2.destroyAllWindows()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    