import cv2

# Fotoğrafı gri tonlamalı (grayscale) olarak yükle
img = cv2.imread("messi.jpg", 0)

# Fotoğrafı bir pencerede göster
cv2.imshow("Ilk Resim", img)

# Bir tuşa basılana kadar bekle
k = cv2.waitKey(0)

if k == 27:
    # Tüm pencereleri kapat
    cv2.destroyAllWindows() 
elif k == ord("s"):
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()
                   
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           
                           