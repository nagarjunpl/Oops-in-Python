# QR Code Generator using Python

import qrcode

image = qrcode.make("Python Programming is fun!")

image.save("py.png")

print("QR code generated successfully!!!")