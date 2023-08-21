import qrcode as qr
from PIL import Image,ImageDraw




img = qr.make('www.google.com')

img.save("some_file.png")
