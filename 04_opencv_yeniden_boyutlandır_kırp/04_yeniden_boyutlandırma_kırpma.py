import cv2

img = cv2.imread("lenna.png")
print("Resim boytu", img.shape) # img.shape resmin yüksekliği genişliği döndürür

cv2.imshow("Orijinal", img)


img_resize = cv2.resize(img,(15,15)) # resize yeniden boyutlandır
print("Resized Img Shape: ", img_resize.shape)

cv2.imshow("Image resized", img_resize ) # imshow resmi pencerede görüntülememizi sağlar

# kırp
img_cropped = img[:200,:300]
cv2.imshow("Kirpilan resim ",img_cropped)


cv2.waitKey(0)
cv2.destroyAllWindows()