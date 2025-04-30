import cv2
import numpy as np


#resim oluştur
img = np.zeros((512,512,3), np.uint8)

cv2.imshow("Sekil", img)



# çizgi
# (resim, başlangıç noktası, bitiş noktası, renk, kalınlık)
cv2.line(img, (100,100),(100,300),(0,255,0), 3 ) # BGR= (255,0,0) = blue
cv2.imshow("Cizgi", img)



# dikdörtgen
#(resim, başlangıç, bitiş  )
cv2.rectangle(img, (100,100), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("Dikdortgen", img)

# çember
#(resim, merkez, yarıçap, renk)
cv2.circle(img, (256,256), 45 , (0,0,255), cv2.FILLED)
cv2.imshow("Cember", img)


# metin
#(resim, yazı, başlangıç noktası, font, renk)
cv2.putText(img, "resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("Text", img)




cv2.waitKey(0)
cv2.destroyAllWindows()






















