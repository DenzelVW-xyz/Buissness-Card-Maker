import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

# Set up Directory

rootdir = os.path.abspath(os.curdir)

try:
    os.mkdir("Results")
    os.chdir("Results")
except FileExistsError:
    os.chdir("Results")

# Data User inputs
qrcode_data = input("Data for QRcode: ")
card_Title = input("Title of the card: ")
logo = input("Path to your logo")

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
Image.new("RGB", (1050, 600), (245, 245, 220)).save("Result.png")
Card_Background = Image.open("Result.png")
create_qr_code(qrcode_data)
code = Image.open("qrcode.png")
code = code.resize((250, 250))
Card_Background.paste(code, (0, 0)) # Add qr code

# Create a title and a dynamically scale to a textbox
Title = ImageDraw.Draw(Card_Background)
font_Size = 65
myFont = ImageFont.truetype(os.path.join(rootdir, "fonts", "Caudex-Bold.ttf"), font_Size)
Textbox = Title.textbbox(xy=(525, 10), text=card_Title, anchor="mt", font=myFont)
max_width = 550
while Title.textlength(text=card_Title, font=myFont) > max_width:
    font_Size -= 1
    myFont = ImageFont.truetype(os.path.join(rootdir, "fonts", "Caudex-Bold.ttf"), font_Size)
Title.text((525, 10), card_Title, fill=(0, 0, 0), font=myFont, anchor="mt") # Add Title

# Add Logo to the top right of the card
logo = Image.open(logo)
logo.resize(250, 250)
Card_Background.paste(logo, (1050, 0))

# Save and cleanup
Card_Background.save("Result.png")
os.remove("qrcode.png")