# gerekli kütüphaneleri ekleyelim
import random
from datetime import datetime
import time
import os
import fnmatch
import pandas as pd
import colorama


# fonksiyon yardımıyla dosya arama işlemi ysapıyoruz
# fonksiyonumuz belitmiş olduğumuz yol üzerindeki dosya içerisinde arama yapıyor
# sonucunda True/False değer döndürüyor ve dosyayı atama işlemi ile dışarıya return ediyor.
from colorama import Fore


def file_search(vote):
    temp = bool
    with os.scandir("D:\\programlama\\python\\AKA-Project\\Project-9.8.22\\abc-word") as tarama:
        for belge in tarama:
            if fnmatch.fnmatch(belge.name, vote):
                document = belge
                temp = True
                break
            else:
                temp = False
    return temp, document

print(" "*15, "👏👏👏  Yazı Yazma Hız Testine HOŞ GELDİNİZ\t👏👏👏\n\n")

# burdaki döngünün amacı harf seçimi ve dosya kontrol işlkemleri için
while True:
    print("\n\nÇıkış için * 'a basın\n\n")
    vote = input("A-Z hangi harf ile test olmak istersiniz veya karışık mı?(abc= karışık):\t")
    if vote == "*":
        print("Çıkış yapıldı!!!")
        break
    vote.upper()
    vote += ".txt"
    re_temp, documents = file_search(vote)
    if re_temp == False:
        print("\nBöyle bir dosya dizinde bulunamadı... Lütfen tekrar deneyin")
    else:
        print(vote+" dosyası bulundu.")
        break

# burada 3-2-1-go yapıp başlangıç değerini alıyoruz
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go!")
time.sleep(0.2)
before = datetime.now()
os.system('cls')

# fonksiyoın yardımı ile bulunan dosyayı pandas yardımı ile okuyorum ve atıyorum
dosya = pd.read_csv(documents)

# bu döngüde ise random sayı üreterek dosya içerisinde random kelime alıyoruz ve çıkış işlemini gerçekleştiriyoruz
while True:
    x = random.randint(0,len(dosya))
    skor = 0
    print(*dosya.iloc[x])
    text=input("Buraya yazın:\t")
    if text == "*":
        break

after = datetime.now()
speed = after - before
seconds = round(speed.total_seconds(),2)
letter_per_second = round(len(text) / seconds,1)

print("\nşu kadar saniyede yazdın : {} seconds.".format(seconds))
print("\n{} saniye başına harf.".format(letter_per_second))
