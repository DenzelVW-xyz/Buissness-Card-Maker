import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Set up Directory
try:
    os.mkdir("Results")
    os.chdir("Results")
except FileExistsError:
    os.chdir("Results")

# User Inputs the URL or data they wanna add to the qrcode
url = input("Data for QRcode: ")

def create_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2)
    
    qr.add_data('Test Data')    
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="beige")
    img.save("qrcode.png")
    
create_qr_code('test')
code = Image.open("qrcode.png")

Image.new("RGB", (1050, 600), (245, 245, 220)).save("Buissness_card_Background.png")
Card_Background = Image.open("Buissness_card_Background.png")
Card_Background.paste(code, (0, 0))
Card_Background.save("temp.png")


