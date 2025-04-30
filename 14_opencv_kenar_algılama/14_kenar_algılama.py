import cv2
import matplotlib.pyplot as plt
import numpy as np


# resmi içe aktar 
img = cv2.imread("london.jpg", 0)

# resmi görselleştriyoruz 
plt.figure(), plt.imshow(img, cmap="gray"), plt.axis("off"), plt.show()

# canny fonksiyonu kenar tespiti için kullanılan bir algoritma
edges  = cv2.Canny(image = img, threshold1=0 , threshold2= 255)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off"), plt.show()


med_val = np.median(img)
print(med_val)

# threshold değerlerini dinamik olarak belirleme (yaygın yaklaşım olduğu için bu şekilde)
low = int(max(0, (1 - 0.33)* med_val))
high = int(min(255, (1 + 0.33)* med_val))
print(low)
print(high)

edges  = cv2.Canny(image = img, threshold1=low , threshold2= high)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off"), plt.show()

# blur
blured_img = cv2.blur(img, ksize= (5,5))
plt.figure(), plt.imshow(blured_img, cmap="gray"), plt.axis("off"), plt.show()


med_val = np.median(blured_img)
print(med_val)

low = int(max(0, (1 - 0.33)* med_val))
high = int(min(255, (1 + 0.33)* med_val))

print(low)
print(high)

edges  = cv2.Canny(image = blured_img, threshold1=low , threshold2= high)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.axis("off"), plt.show()



















