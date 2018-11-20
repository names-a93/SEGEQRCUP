# pip install Pillow
# pip install qrcode

from PIL import Image
import getpass
import os
import qrcode

print("Please enter text to generate into qrcode")
text_data = getpass.getpass()

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

qr.add_data(text_data)
qr.make(fit=True)

img = qr.make_image()
img.save("temp_image.png")

show_img = Image.open("temp_image.png")
show_img.show()

print("Press enter to cleanup")
raw_input()
os.remove("temp_image.png")
