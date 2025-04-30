import cv2
import os

# Mevcut klasördeki dosyaları listele
files = os.listdir()

# JPG uzantılı dosyaları bir listeye ekle
img_path_list = [file for file in files if file.endswith("jpg")]
print(img_path_list)

cat_cascades = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")


# Görüntüleri sırayla göster
for j in img_path_list:
    print(j)
    img = cv2.imread(j)
    # Hata kontrolü: Görüntü okunamazsa atla
    if img is None:
        print(f"Dosya okunamadı: {i}")
        continue
    cat_rect = cat_cascades.detectMultiScale(img, scaleFactor=1.04,minNeighbors=4)
    for (i,(x,y,w,h)) in enumerate(cat_rect):
        cv2.rectangle(img, (x,y), (x+w , y+h), (255,0,0), 5)
        cv2.putText(img, "Kedi {}".format(i+1), (x,y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL , 0.55, (0,255,255))
   
    
    # Görüntüyü göster
    cv2.imshow(j, img)
    
    # 'q' tuşuna basıldığında bir sonraki görüntüye geç
    if cv2.waitKey(0) & 0xFF == ord("q"):
        continue

# Tüm pencereleri kapat
cv2.destroyAllWindows()