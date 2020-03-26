# install pypng
# install pyqrcode
# install pillow
# install pyzbar

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

data = input('Enter data : ')
def generate_qrcode(data):
    qr = pyqrcode.create(data)
    qr.png('qrcode.png' , scale=10)

def read_and_verify_qrcode(data) :
    d = decode(Image.open('qrcode.png'))
    qrdata = str(d[0].data)[2:-1]
    if data == qrdata :
        print("Confirmed QR is valid ")
    else:
        print("QR is invalid")

generate_qrcode(data)
read_and_verify_qrcode(data)