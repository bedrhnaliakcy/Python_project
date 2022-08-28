import qrcode
from PIL import Image
img = qrcode.make("https://www.akaeskisehir.com/Anasayfa")
img.save("QrCode.png")