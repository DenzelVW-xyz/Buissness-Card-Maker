import qrcode
from PIL import Image
import os

# Set up Directory
try:
    os.mkdir("Results")
    os.chdir("Results")
except FileExistsError:
    os.chdir("Results")
    

url = input("Please input your full URL: ")

qrcode.make(url).save("qrcode.png")
code = Image.open("qrcode.png")

Image.new("RGB", (1050, 600), (245, 245, 220)).save("Buissness_card_Background.png")
Card_Background = Image.open("Buissness_card_Background.png")
Card_Background.paste(code, (0, 0))
Card_Background.save("temp.png")


