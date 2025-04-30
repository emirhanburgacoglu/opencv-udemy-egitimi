# %% spyder tanıtımı 
print("hello world")

# %% veriables

integer = 10
double = 12.3

print(integer)
print(double)

# 4 işlem özellikleri

pi_number = 3.14
coefficent = 2

toplam = pi_number + 1
sub = pi_number - 1
multi = pi_number * coefficent
divide = pi_number / coefficent

# print 

print("Toplam :", toplam)

print("toplam {} ve fark {}".format(toplam,sub))

print("Çarpma: %.1f, bölme: %.4f" % (multi,divide))


# Değişkenler arası dönüşüm

carpma_int = int(multi)
print(carpma_int)

tamsayi_float = float(integer)
print(tamsayi_float)

# String karakter dizileri

string = "Merhaba Dünya"
print(string)


resim_yolu = "veri" + "\\" + "img" + ".png"
print(resim_yolu)

# %% python temel sözdizimi
# büyük ve küçük harf

temel = 6
TEMEL = 7

#yorum 
"""
bu bölümde söz dzimi 
    - büyük küçük harf
    - yorum
    - girinti
    - anahtar Kelimeler

"""
#girinti

if 5<10:
    print("yes")
else:
    print("no")

# anahtar kelimeler
de = 4
# def = 4

# sayı değişkeni

sayi1 = 5
sayi2 = 2

# 1sayi = 7

# %% liste

"""
- bileşik veri türüdür ve çok yönlüdür
- [1,"a",1.0]
- farklı veri tiplerinin içerisinde barındırabilir

"""
liste = [1,2,3,4,5,6]
print(type(liste))

hafta = ["pazartesi", "salı","çarşamba", "perşembe"]
#ilk eleman
print(hafta[0])
#son eleman
print (hafta[3])
print(len(hafta)) #eleman sayısı


# listenin 2-3-4 elemanlarını yazdırma
print(hafta[1:4]) # 1 dahil 4 dahil değildir

# sayı listesi

sayi_listesi = [1,2,3,4,5,6]
sayi_listesi.append(7)
print(sayi_listesi)

# listeden eleman çıkarma
sayi_listesi.remove(4)
print(sayi_listesi)

# listeyi ters çevirme
sayi_listesi.reverse()
print(sayi_listesi)

# listeyi sırala
sayi_listesi = [1,56,54,3,6,3,2,5,578]
sayi_listesi.sort()
print(sayi_listesi)

# %% tuple

"""
değiştirilemez ve sıralı bir bir veri tipidir
(1,2,3)

"""
tuple_veritipi = (1,2,3,3,4,5,6)
#ilk eleman
print(tuple_veritipi[0])

# 2. indexten sonraki elemanları yazdır 
print(tuple_veritipi[2:])

# count eleman
print(tuple_veritipi.count(3))

tuple_xyz = (1,2,3)
x,y,z = tuple_xyz
print(x,y,z)

# %% deque

from collections import deque 
dq = deque(maxlen = 3)

dq.append(1) # 1 ekle sonuna [1]
print(dq)

dq.append(2) # 2 ekle sonuna [1, 2]
print(dq)

dq.append(3) # 3 ekle sonuna [1,2,3]
print(dq)


dq.append(4) # 4 ekle sonuna [2,3,4]
print(dq)

dq = deque(maxlen= 3)

dq.append(1) # 1 ekle sonuna [1]
print(dq)

dq.append(2) # 2 ekle sonuna [1, 2]
print(dq)

dq.appendleft(3) # 3 ekle başına [3,1,2]
print(dq)


dq.clear()
print(dq)

# %% dictionary 
"""
- bir çeşit karma tablo türüdür
- anahtar ve değer çiftlerinden oluşr 
- {"anahtar" : değer}
 
"""
dictionary = {"İstanbul": 34,
              "İzmir"   : 35,
              "Konya"   : 42}

print(dictionary)

#istanbul anahtarının değirine bakmak istersek
print(dictionary["İstanbul"])

#anahtarlar
print(dictionary.keys())

#değerler 
print(dictionary.values())

# %% koşullu ifadeler if else statement

"""
bir bool ifadesine göre doğru ya da yanlış olarak değerlendirilmesine 
olarak farklı hesaplamalar veya eylemler gerçekleştiren eylemlerdir

"""
bool1 = True
bool2 = False

sayi1 = 12.0
sayi2 = 20.0

if (sayi1 < sayi2):
    print("sayı 1: {} küçüktür sayı 2: {}".format(sayi1, sayi2))
elif (sayi1 > sayi2):
    print("sayı 1: {} büyüktür sayı 2: {}".format(sayi1, sayi2))
else: 
    print("sayı 1: {} eşittir sayı 2: {}".format(sayi1, sayi2))


liste = [1,2,3,4,5]
deger = 32

if deger in liste:
    print("{} değeri listenin içerisindedir".format(deger))
else: 
    print("{} değeri listenin içerisinde değildir".format(deger))



dictionary = {"Türkiye"   : "Ankara",
              "İngiltere" : "Londra",
              "İspanya"   : "Madrid"}

keys = dictionary.keys()
deger = "Türkiye"
if deger in keys:
    print("Evet")
else:
    print("Hayır")
  
    
bool1 = False
bool2 = False
if bool1 and bool2:
    print("Doğru")
else: 
    print("Yanlış")

# %% Döngüler Loops

"""
- bir dizi üzerinde yineleme yapmak için kullanılan yapılardır
- diziler: liste, tuple, string, sözlük, numpy pandas veri tipleri

"""

for i in range(1,12): # [1,2,3,4,5...........]
    print(i)

list = [1,2,3,45,67,65,7,8,437,8,6]
sum(list)
toplam = 0
for i in list:
    toplam = toplam + i
    
print(toplam)

tup1 = ((1,2,3),(3,4,5))
for x,y,z in tup1:
    print(x,y,z)

# while 

i = 0
while (i<4):
    print(i)
    i+=1

list = [1,23,4,5,6,7,8,8,89,8]
limit = len(list)

her = 0 
hesapla = 0
while her <limit:
    hesapla = hesapla + list[her]
    her +=1
print(hesapla)
 
# %% fonksiyonlar 
"""
- karmaşık işlemleri toplar ve tek adımda yapnanızı sağlar
- şablon
- düzenleme
"""
# kullanıcı tarafında tanımlanan fonk

def daireAlanı(r):
    
    """
    Parameters
    ----------
    r : int. daire yarıcapı

    Returns 
    -------
    daire_alani : float - alanı

    """ 
    pi = 3.14
    daire_alanı = pi* (r**2)
    return daire_alanı
    
daireAlanıDeğişkeni = daireAlanı(5)

print(daireAlanıDeğişkeni)

def daireCevre(r,pi = 3.14):
    """

    Parameters
    ----------
    r : int. dairenin yarıcapı
    pi :float - pi sayısı
        DESCRIPTION. The default is 3.14.

    Returns
    -------
    daire_cevresi : float - daire çevre.

    """
    daire_cevresi = 2*pi*r
    return daire_cevresi

daireCevre(4)

katsayi = 5
def katsayiCarpimi():
    global katsayi
    print(katsayi * katsayi)

katsayiCarpimi()
print(katsayi)

# boş fonksiyonlar

def bos():
    pass
    
# built in function
list = [1,2,3,4,5]

print(len(list))
print(str(list))
list2 = list.copy()

print(list2)
print(max(list))
print(min(list))

# lamda function
"""
- ileri seviyedir
- küçük ve anonim bir işlmedir

"""
def carpma(x,y,z):
    
    return x*y*z 
sonuc = carpma(2,3,4)
print(sonuc)

# aynı işlem with lambda
fonksiyon_lambda = lambda x,y,z : x*y*z
fonksiyon_lambda(2,3,4)


# %% yield 
"""
- iterasyon (yineleme)
- generator
- yield
"""
list = [1,2,3]
for i in list:
    print(i)
"""
generator yinelecileri
generator değerleri bellekte saklamaz yeri gelince anında üretirler

"""
generator = (x for x in range(1,4))

for i in generator:
    print(i)

"""
fonksiyon eğer return olarak generator döndürecek ise 
bunu return yerine yield keyword ü ile yapar
"""
def createGenerator():
    list = range(1,4)
    for i in list:
        yield i


generator = createGenerator()
print(generator)
for i in generator:
    print(i)


# %% numpy kütüphanesi 
"""
- matrisler için hesaplama kolaylığı sağlar


"""
import numpy as np

# 1*15 boyuyunda bir array-dizi

dizi = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

print(dizi)

print(dizi.shape) # array'in boyutu

dizi2 = dizi.reshape(3, 5) # reshape 3*5 şeklinde matrise çevirir

print(dizi2)

print("Şekil: ", dizi2.shape)
print("Boyut: ", dizi2.ndim)
print("veri tipi: ", dizi2.dtype.name)
print("Boy: ", dizi2.size)

# array type 

print("Type: ", type(dizi2))

# 2 Buyutlu array
dizi2D = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,6]])
print(dizi2D)

# sıfırlardan oluşan bir array

sifir_dizi = np.zeros((3,4))
print(sifir_dizi)

# birlerden oluşan dizi
bir_dizi = np.ones((3,4))
print(bir_dizi)

# boş array

bos_dizi = np.empty((3,4))
print(bos_dizi)


# arange(x,y,basamak)
dizi_aralik = np.arange(10,50,5)
print(dizi_aralik)

# linspace(x,y,basamak)
dizi_bosluk = np.linspace(10,20,5)
print(dizi_bosluk)

# float array
float_array = np.float32([[1,2],[3,4]])
print(float_array)

# matematiksel işlemler
a = np.array([1,2,3])
b = np.array([4,5,6])

print(a-b)
print(a+b)
print(a**2)

# dizi elemanı toplma
print(np.sum(a))

# max değer 
print(np.max(a))

# min değer 
print(np.min(a))

# mean ortalama 
print(np.mean(a))

# medyan 
print(np.median(a))

# rastgele sayı üretme [0,1] arasında sürekli uniform 3*3

rastgele_dizi = np.random.random((3,3))
print(rastgele_dizi)

# indeks 
dizi = np.array([1,2,3,4,5,6,7])
print(dizi[0])

# dizinin ilk dört elemanı
print(dizi[0:4])

# dizinin tersini alma
print(dizi[::-1])

dizi2D = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(dizi2D)

# dizinin 1. satır ve 1. sütünunda bulunan elemanı 

print(dizi2D[1,1])

# 1. sütün sütün ve tüm satırlar
print(dizi2D[:,1])


# satır 1, sütün 1,2,3
print(dizi2D[1,1:4])


#dizinin son satır ve tüm sütünları
print(dizi2D[-1,:])

# diziyi vektor haline getirme
dizi2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(dizi2D)

vektor = dizi2D.ravel() # diziyi vektor haline getirir
print(vektor)

maksimum_sayinin_indeksi = vektor.argmax()
print(maksimum_sayinin_indeksi)

# %% pandas
import pandas as pd
"""
- hızlı güçlğ ve esnek 
- 

"""
# sözlük oluştur
dictionary = {"isim" : ["ali", "veli", "kenan", "murat", "ayşe", "hilal"],
              "yaş"  : [15, 17, 18, 34, 34, 66],
               "maas": [100,150,350,543,789,765]}


veri = pd.DataFrame(dictionary)
print(veri)

# ilk 5 satır
print(veri.head())

print(veri.columns)

# veri bilgisi
print(veri.info())

# istatistiksel özellikler
print(veri.describe())

# yaş sütünu 
print(veri["yaş"])

# sütün eklemek 
veri["sehir"] = ["Ankara", "İstanbul", "Konya", "İzmir", "Bursa", "Antalya"]
print(veri)

# yaş sütünu 
print(veri.loc[:,"yaş"])

# yaş sütünu ve 3 satır 
print(veri.loc[:2,"yaş"])

# yaş ve sehir arası sütünu ve 3 satır 
print(veri.loc[:2, "yaş":"sehir"])

# isim ve şehir ilk 3 satır
print(veri.loc[:2, ["isim","sehir"]])

# satırları tersen yazdır
print(veri.loc[::-1,:])

# yas sütünu with iloc
print(veri.iloc[:,1])

# ilk üç satır , yaş ve isim 
print(veri.iloc[:3,[0,1]])


# filtreleme   

dictionary = {"isim" : ["ali", "veli", "kenan", "murat", "ayşe", "hilal"],
              "yaş"  : [15, 17, 18, 34, 34, 66],
              "maas" : [100,150,350,543,789,765],
              "sehir": ["İzmir", "Ankara", "Konya", "Ankara", "Ankara", "Antalya"]}

veri = pd.DataFrame(dictionary)
print(veri)

# ilk olarak yaşşa göre bir filtre yas > 22
filtre1 = veri.yaş > 22

filtrelenmiş_veri = veri[filtre1]
print(filtrelenmiş_veri)


# ortalama yaş
ortalama_yaş = veri.yaş.mean()
veri["YAS_GRUBU"] = ["küçük" if ortalama_yaş > i else "büyük" for i in veri.yaş ]

print(veri)

# birleştirme

sozluk1 = {"isim" : ["ali","veli","kenan"],
           "yas"  : [15,16,17],
           "sehir": ["İzmir","Ankara","Konya"]}
veri1 = pd.DataFrame(sozluk1)

sozluk2 = {"isim" : ["murat","ayşe","hilal"],
           "yas"  : [33,45,66],
           "sehir": ["Ankara","Ankara","Antalya"]}
veri2 = pd.DataFrame(sozluk2)

# verileri dikeyde birleştirme

veri_dikey = pd.concat([veri1, veri2], axis=0)
print(veri_dikey)


# verileri yatayda birleştirme

veri_yatay = pd.concat([veri1,veri2], axis=1)
print(veri_yatay)

# %% matplotlib kütüphanesi
  
"""
- görselleştirme

"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4])
y = np.array([4,3,2,1])
plt.figure()
plt.plot(x, y, color="red", alpha = 0.7, label = "line")
plt.scatter(x, y, color = "blue",alpha=0.4,label= "scatter")
plt.title("Matplotlib")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.xticks([0,1,2,3,4,5])
plt.legend()
plt.show()

fig, axes = plt.subplots(2,1, figsize = (9,7))
fig.subplots_adjust(hspace= 0.5)

x = [1,2,3,4,5,6,7,8,9,10]
y = [10,9,8,7,6,5,4,3,2,1]

axes[0].scatter(x,y)
axes[0].set_title("sub-1")
axes[0].set_ylabel("sub-1 y")
axes[0].set_xlabel("sub-1 x")

axes[1].scatter(y,x)
axes[1].set_title("sub-1")
axes[1].set_ylabel("sub-1 y")
axes[1].set_xlabel("sub-1 x")
plt.show()


# random sayılardan resim oluşturma
plt.figure()
img = np.random.random((50,50))
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.show()


# %% OS kütüphanesi 
"""
- bilgisayarımızdaki dosyalarda dolaşmamızı sağlar
"""
import os

print(os.name)

currentDir = os.getcwd()
print(currentDir)

# new folder
folder_name = "new_folder"
os.mkdir(folder_name)

# oluşturulan dosyanın adını değiştirme
new_folder_name = "new_folder_2"
os.rename(folder_name, new_folder_name)

os.chdir(currentDir+ "\\" + new_folder_name)
print(os.getcwd())

os.chdir(currentDir)
print(os.getcwd())

files = os.listdir()
print(files)
for f in files:
    if f.endswith(".py"):
        print(f)

os.rmdir(new_folder_name)

for i in os.walk(currentDir):
    print(i)
os.path.exists("python_hatırlatma.py")

os.rmdir("01_resim_içe_Aktarma.py")

















