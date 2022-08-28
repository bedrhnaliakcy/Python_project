# gerekli kütüphaneler yükleniyor
import pandas as pd
from matplotlib import pyplot as plt

# veriyi okuyoruz
covid19 = pd.read_excel("corona.xltx")
# veri setinin bozulmalara karşın kopyasını alıyoruz
covid19_copy = covid19.copy()
# gereksiz verileri siliyoruz
covid19_copy.drop(["toplam_vaka", "toplam_vefat"], axis="columns", inplace=True)
# Grafik işlemleri başlatılıyor...

f=plt.figure()
#koordinatlar
axes1=f.add_axes([0.1,0.1,0.9,0.9])
axes2=f.add_axes([0.6,0.5,0.3,0.3])

#Grafik başlıkları
axes1.set_title("Türkiye Covid-19 Vaka ve İyileşme Tablosu")
axes2.set_title("Türkiye Covid-19 Vefat Tablosu")

#y ekseni başlıkları
axes1.set_ylabel("Tarih")
axes2.set_ylabel("Tarih")

#x ekseni başlıkları
axes1.set_xlabel("Vaka ve İyileşen")
axes2.set_xlabel("Vefat")

#1. Grafikteki veriler
axes1.plot(covid19_copy.haftalık_vaka,covid19_copy.tarih,color="blue")
axes1.plot(covid19_copy.haftalık_iyilesen,covid19_copy.tarih,color="red")
# 2. Grafikteki veri
axes2.plot(covid19_copy.haftalık_vefat,covid19_copy.tarih, color="black")
# Ekrana yaz
plt.show()
