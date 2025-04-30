import cv2
import matplotlib.pyplot as plt
import numpy as np

# Resmi içe aktar
coin = cv2.imread("coins.jpg")
plt.figure(), plt.imshow(cv2.cvtColor(coin, cv2.COLOR_BGR2RGB)), plt.axis("off"), plt.show()

# Lpf: Blurring
coin_blur = cv2.medianBlur(coin, 13)
plt.figure(), plt.imshow(cv2.cvtColor(coin_blur, cv2.COLOR_BGR2RGB)), plt.axis("off"), plt.show()

# Grayscale
coin_gray = cv2.cvtColor(coin_blur, cv2.COLOR_BGR2GRAY)
plt.figure(), plt.imshow(coin_gray, cmap="gray"), plt.axis("off"), plt.show()

# Binary threshold
ret, coin_thresh = cv2.threshold(coin_gray, 65, 255, cv2.THRESH_BINARY)
plt.figure(), plt.imshow(coin_thresh, cmap="gray"), plt.axis("off"), plt.show()

# Açılma (Morphological Opening)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(coin_thresh, cv2.MORPH_OPEN, kernel, iterations=2)
plt.figure(), plt.imshow(opening, cmap="gray"), plt.axis("off"), plt.show()

# Nesneler arası distance bulma
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
plt.figure(), plt.imshow(dist_transform, cmap="gray"), plt.axis("off"), plt.show()

# Ön plan (foreground) tespiti
ret, sure_foreground = cv2.threshold(dist_transform, 0.4 * np.max(dist_transform), 255, 0)
sure_foreground = np.uint8(sure_foreground)
plt.figure(), plt.imshow(sure_foreground, cmap="gray"), plt.axis("off"), plt.show()

# Arka plan (background) tespiti
kernel = np.ones((3,3), np.uint8)
sure_background = cv2.dilate(opening,kernel, iterations=3)
sure_background = np.uint8(sure_background)
plt.figure(), plt.imshow(sure_background, cmap="gray"), plt.axis("off"), plt.show()

# Bilinmeyen alan (unknown) hesaplama
unknown = cv2.subtract(sure_background, sure_foreground)
plt.figure(), plt.imshow(unknown, cmap="gray"), plt.axis("off"), plt.show()

# Marker oluşturma
ret, markers = cv2.connectedComponents(sure_foreground)
markers = markers + 1  # Arka planın farklı renkte olması için artır
markers[unknown == 255] = 0  # Bilinmeyen alanları sıfırla

# Watershed uygulama
markers = cv2.watershed(coin, markers)
coin[markers == -1] = [255, 0, 0]  # Kenarları kırmızı yap

plt.figure(), plt.imshow(markers, cmap="gray"), plt.axis("off"), plt.title("Watershed Sonucu"), plt.show()















