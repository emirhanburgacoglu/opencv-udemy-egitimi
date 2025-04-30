import cv2
import numpy as np
from collections import deque

# nesne merkezini depolayacak veri tipi
buffer_size = 16
pts = deque(maxlen=buffer_size)

# mavi renk aralığı 
blue_lower = (84, 98, 0)
blue_upper = (179, 255, 255)

#capture
cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 480)

if (cap.isOpened()):
    while True:
        ret, img_original = cap.read()
        if not ret:
            print("Frame does not exits")
            break
        else:
            #blur
            blurred = cv2.GaussianBlur(img_original ,(11,11), 0)
            
            #hsv
            hsv = cv2.cvtColor(blurred , cv2.COLOR_BGR2HSV)
           
            cv2.imshow("HSV Image", hsv)
            
            # mavi için maske oluştur
            mask = cv2.inRange(hsv, blue_lower, blue_upper)
            cv2.imshow("Mask", mask)
            
            # maskenin etrafında kalan gürültüleri sil
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)
            cv2.imshow("Mask + Erozyon ve genişleme", mask)
            
            # kontur
            contours,_ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            center = None
            
            if len(contours) > 0:
                # en büyük contouru al
                for c in contours: 
                
                    #dikdörtgene çevir
                    rect = cv2.minAreaRect(c)
                    
                    ((x,y),(width, height), rotation) = rect
                    s = "x:{}, y: {}, width: {}, height: {}, rotation: {}".format(np.round(x),np.round(y), np.round(width), np.round(height), np.round(rotation))
                    print(s)
                    
                    box = cv2.boxPoints(rect)
                    box = np.int64(box)
                    
                    # moment
                    M = cv2.moments(c)
                    center = (int(M["m10"]/ M["m00"]), int(M["m01"]/M["m00"]))
                    
                    # konturu çizdir sarı
                    
                    cv2.drawContours(img_original, [box] , 0, (0,255,255), 4)
                    
                    # merkeze bir tane nokta çizdir
                    
                    cv2.circle(img_original , center, 5, (255,0,255), -1)
                    
                    # bilgileri ekrana yazdır
                    
                    cv2.putText(img_original, s, (50,50) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 1, (0,0,0), 2)
                    
                # deque
                pts.appendleft(center)
                for i in range(1,len(pts)):
                    if pts[i-1] is None or pts[i] is None:
                        continue
                    cv2.line(img_original , pts[i-1] , pts[i], (0,255,0) , 3)
               
                cv2.imshow("Original Tespit", img_original )
           
                
       
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
else: 
    print("Kamere does not opened")

cap.release()
cv2.destroyAllWindows()
