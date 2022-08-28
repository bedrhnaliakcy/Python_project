import qrcode
from PIL import Image
img = qrcode.make("https://github.com/bedrhnaliakcy")
img.save("QrCode.png")
