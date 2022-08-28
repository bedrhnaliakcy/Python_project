# ses dosyalarını okuma, yazma, dil ve diğer ayarlar için kullanacağımız kütüphane
from gtts import gTTS
# os yardımı ile dosya içerisindeki .mp3 dosyadını açıyor.
import os

# ses dosyasına dönüştürülecek metin
mytext = input("Okunulacak metni giriniz:\t")

# sesin dili
language = 'tr'
#   metni okuyup kaydediyor
#           metin           dil            hızı
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("test-gtts.mp3")

# kaydedilen konuşmayı açıyor.
os.system("test-gtts.mp3")

"""
bu yazılım 'gtts' kütüphanesi ile yapılmıştır.
bir sonra ki yazılımda bunu pyttsx3 ile yapacağız.
"""