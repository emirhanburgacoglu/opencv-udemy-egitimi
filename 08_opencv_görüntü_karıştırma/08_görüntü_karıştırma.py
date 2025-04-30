import cv2
import matplotlib.pyplot as plt

# karıştırma


img_1 = cv2.imread("img1.JPG")
img_1 = cv2.cvtColor(img_1 , cv2.COLOR_BGR2RGB)

img_2 = cv2.imread("img2.JPG")
img_2 = cv2.cvtColor(img_2 , cv2.COLOR_BGR2RGB)

print(img_1.shape)
print(img_2.shape)

img_1 = cv2.resize(img_1,(600,600))
print(img_1.shape)
img_2 = cv2.resize(img_2,(600,600))
print(img_2.shape)

plt.figure()
plt.imshow(img_1)

plt.figure()
plt.imshow(img_2)

# karıştırılmış resim = alpha * img_1 + beta * img_2
blended = cv2.addWeighted(src1= img_1 , alpha = 0.5, src2 = img_2 , beta = 0.5, gamma= 0)

plt.figure()
plt.imshow(blended)
plt.show()













