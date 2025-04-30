import cv2
import numpy as np
# resmi içe aktar
img = cv2.imread("lenna.png")
cv2.imshow("Orijinal Resim", img)

# dikey birleştirme 
hor_img = np.hstack((img,img))
cv2.imshow("Horizontal Resim ", hor_img)

# yatay birleştirme 
ver_img = np.vstack((img,img))
cv2.imshow("Vertical Resim", ver_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

