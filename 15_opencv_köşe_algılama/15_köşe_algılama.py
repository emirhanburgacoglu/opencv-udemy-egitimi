import cv2
import matplotlib.pyplot as plt
import numpy as np

# Resmi içe aktar
img = cv2.imread("sudoku.jpg", 0)

# Görüntüyü float32 formatına dönüştür
img = np.float32(img)
print(img.shape)

plt.figure(),plt.imshow(img, cmap="gray"), plt.axis("off"), plt.show()

# Harris köşe algılama
# Görüntüyü algılamak için cv2.cornerHarris kullanıyoruz
dst = cv2.cornerHarris(img, 2, 3, 0.04)

plt.figure(),plt.imshow(dst, cmap="gray"), plt.axis("off"), plt.show()

# Küçük bir değerle, köşeleri tespit etmeden önce sonuçları artırıyoruz
dst = cv2.dilate(dst, None)

# Köşe tespitlerini renkli olarak işaretle
img[dst > 0.01 * dst.max()] = 255

# Sonuçları görselleştir
plt.figure(),plt.imshow(img, cmap="gray"), plt.axis("off"), plt.show()