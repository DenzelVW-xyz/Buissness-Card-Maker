# Import Modules
from PIL import Image, ImageDraw, ImageFont
import qrcode
import os

# Set up Directory

root_dir = os.path.abspath(os.curdir)

try:
    os.mkdir("Results")
    os.chdir("Results")
except FileExistsError:
    os.chdir("Results")

# Data User inputs
qrcode_data = input("Data for QRcode: ")
card_title = input("Title of the card: ")
logo = input("Path to your logo: ")
remove_background = bool(input("Would you like to remove logo background?\n(Y/N): ").strip().upper() == "Y")

# Prepare Background removal model.
if remove_background == True:
    print("Importing rembg module...", flush=True)
    from rembg import remove, new_session
    print("Preparing AI model...", flush=True)
    session = new_session("u2net")
    print("AI model ready!")


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

# Create an the background, add the qr_image.
Image.new("RGB", (1050, 600), (245, 245, 220)).save("Result.png")
card_background = Image.open("Result.png").convert("RGBA")
create_qr_code(qrcode_data)
qr_image = Image.open("qrcode.png")
qr_image = qr_image.resize((250, 250))
card_background.paste(qr_image, (0, 0)) # Add qr_image

# Create a title and a dynamically scale to a textbox
Title = ImageDraw.Draw(card_background)
font_size = 65
font = ImageFont.truetype(os.path.join(root_dir, "fonts", "Caudex-Bold.ttf"), font_size)
max_width = 550
while Title.textlength(text=card_title, font=font) > max_width:
    font_size -= 1
    font = ImageFont.truetype(os.path.join(root_dir, "fonts", "Caudex-Bold.ttf"), font_size)
Title.text((525, 10), card_title, fill=(0, 0, 0), font=font, anchor="mt") # Add Title

# Add Logo to the top right of the card
try:
    logo = Image.open(logo).convert("RGBA")
except FileNotFoundError:
    try:
        logo = Image.open(os.path.join(root_dir, logo)).convert("RGBA")
    except FileNotFoundError:
        print("Image you provided does not exist.")


# Resize while maintaining aspect ratio
logo.thumbnail((250, 250), Image.Resampling.LANCZOS)

if remove_background:
    print("Removing Logo Background...")
    logo = remove(logo, session=session)

# Calculate top-right position dynamically
x = card_background.width - logo.width
y = 0

# Paste logo
card_background.paste(logo, (x, y), logo)

# Save and cleanup
card_background.save("Result.png")
os.remove("qrcode.png")