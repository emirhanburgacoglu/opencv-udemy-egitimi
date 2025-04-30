import cv2
import matplotlib.pyplot as plt
import numpy as np

# Ana görüntüyü içe aktarma
chos = cv2.imread("chocolates.jpg", 0)
plt.figure(), plt.imshow(chos, cmap="gray"), plt.axis("off"), plt.title("Cikolatalar"), plt.show()

# Aranacak olan görsel
cho = cv2.imread("nestle.jpg", 0)
plt.figure(), plt.imshow(cho, cmap="gray"), plt.axis("off"), plt.title("Nestle"), plt.show()

# ORB tanımlayıcı
orb = cv2.ORB_create()

# Anahtar nokta tespiti ORB ile
kp1, des1 = orb.detectAndCompute(cho, None)
kp2, des2 = orb.detectAndCompute(chos, None)

# BF Matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

# Noktaları eşleştir
matches = bf.match(des1, des2)

# Mesafeye göre sırala
matches = sorted(matches, key=lambda x: x.distance)

# Eşleşen resimleri görselleştirme
plt.figure()
img_match = cv2.drawMatches(cho, kp1, chos, kp2, matches[:20], None, flags=2)
plt.imshow(img_match), plt.axis("off"), plt.title("ORB Eşleşmeleri"), plt.show()

# SIFT tanımlayıcı
sift = cv2.SIFT_create()

# Anahtar nokta tespiti SIFT ile
kp1, des1 = sift.detectAndCompute(cho, None)
kp2, des2 = sift.detectAndCompute(chos, None)

# BF Matcher (SIFT için)
bf = cv2.BFMatcher(cv2.NORM_L2)

# Noktaları eşleştir (KNN ile)
matches = bf.knnMatch(des1, des2, k=2)

# En iyi eşleşmeleri bul
best_match = []
for match1, match2 in matches:
    if match1.distance < 0.75 * match2.distance:
        best_match.append([match1])

# SIFT eşleşmelerini görselleştirme
plt.figure()
sift_matches = cv2.drawMatchesKnn(cho, kp1, chos, kp2, best_match, None, flags=2)
plt.imshow(sift_matches), plt.axis("off"), plt.title("SIFT Eşleşmeleri"), plt.show()











