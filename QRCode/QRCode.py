# author :: HimelSaha

import qrcode

url = input("Enter valid URL to create the QR Code for: ")    # prompting user for url
print("creating...")
qr_image = qrcode.make(url)                                   # qrcode created
qr_image.save("qr_code_generated.png", "PNG")                 # qrcode image created using PIL
print()
print("Operation done successfully! QR Code has been created.")