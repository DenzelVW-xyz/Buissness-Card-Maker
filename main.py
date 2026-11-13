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
qrcode_data = input("Data for QRcode: ")

# Function that creates the qrcode and saves it as an image
def create_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2)
    
    qr.add_data(data)    
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="beige")
    img.save("qrcode.png")

# Create an the background, add the qr code.
def background_init():
    Image.new("RGB", (1050, 600), (245, 245, 220)).save("Business_card_Background.png")

background_init()
Card_Background = Image.open("Business_card_Background.png")
create_qr_code(qrcode_data)
code = Image.open("qrcode.png")

Card_Background.paste(code, (0, 0))
Card_Background.save("temp.png")