from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_blank_image(width, height):
    return Image.new("L", (width, height), "white")  # "L" mode for monochrome images

def image_to_hex_bitmap(image):
    pixels = list(image.getdata())
    hex_bitmap = ', '.join(['0X{:02X}'.format(pixel) for pixel in pixels])
    return hex_bitmap

def createImage():


    width, height = 250, 122
    i = create_blank_image(width, height)

    Im = ImageDraw.Draw(i)
    mf = ImageFont.truetype('fonts/ShortBaby-Mg2w.ttf', 25)
    Im.text((15, 15), "Hello", 0, font=mf)  # Use 0 for monochrome (black) color

    hex_bitmap = image_to_hex_bitmap(i)
    print(hex_bitmap)
    return hex_bitmap

