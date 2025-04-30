"""
1) veri seti oluştur
  -->  pozitif ve negatif resimler
2) cascade programı indir
3) cascade oluştur
4) cascade kullanarak tespit algoritması yaz

"""
import cv2
import os
# resim depo klasörü
path = "images"

# resim boyutu (amacı resimleri yeeniden boyutlandırmada kullanılacak)
img_width = 180
img_height = 120

# video Capture
cap = cv2.VideoCapture(0)

# amacı daha düşük çözünürlük kullanarak işlem süresi ve performası iyileştirmek
cap.set(3, 640)
cap.set(4, 480)
cap.set(10,180)

global countFolder
def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists(path + str(countFolder)):
        countFolder += 1
    os.makedirs(path + str(countFolder))
saveDataFunc()

count = 0
count_save = 0

while True:
    ret , frame= cap.read()
    frame = cv2.flip(frame,1)
    if ret:
        frame = cv2.resize(frame, (img_width,img_height))
        if count % 5 == 0:
            cv2.imwrite(path+ str(countFolder)+ "/" + str(count_save)+"_"+".png",frame)
            count_save +=1 
            print(count_save)
        count +=1
            
        cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
        



















