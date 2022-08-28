import pyttsx3 as pyttsx3

engine = pyttsx3.init()

"""   RATE    """
rate = engine.getProperty('rate')
print("Mevcut ses hız seviyesi:\t",rate)
engine.setProperty('rate', 200)

"""     VOLUME      """
volume = engine.getProperty('volume')
print("Mevcut ses seviyesi:\t",volume)
engine.setProperty('volume', 0.5)

"""     VOİCE       """
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # erkek ses
#engine.setProperty('voice', voices[1].id) # kadın ses

engine.say("merhaba dünya")
engine.say('Şuan ki konusma hizim ' + str(rate))
engine.runAndWait()
engine.stop()

"""     Save        """
# burada kaydedilen ses ⬇️kısımdır. burası ise ⬇ dosya adı.
engine.save_to_file("ı make some time alone", "test-pyttsx3.mp3")
engine.runAndWait()



"""
bu yazılım 'pyttsx3' kütüphanesi ile yazılacaktır.

Adımlar:
    1- kütüphane ekleme
    2- değişken tanımlama ve pyttsx3.init() nesnesini oluşturma.
    3- konuşmaya çevirelecek metni alıp .say() fonksiyonun içerisine at
    4- opsiyonel- 'RATE-HIZ' fonksiyonu ile (mevcut hız - yeni hız) ayarlamalar yapılacak
    5- opsiyonel- 'VOLUME-SES' fonksiyonu ile (mevcut ses - yeni ses) ayarlamalar yapılacak
    6- opsiyonel- 'VOICE-SES' fonksiyonu ile (0=erkek - 1=kadın) ayarlamalar yapılacak
    7- opsiyonel- 'SAVE-KAYDET' fonksiyonu ile (sesi bir dosyaya keydekme) ayarlamalar yapılacak
    8- şimdi Çalıştır-ve-Bekle
"""