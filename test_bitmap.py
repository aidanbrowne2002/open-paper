from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_blank_image(width, height):
    return Image.new("L", (width, height), "white")  # "L" mode for monochrome images

def image_to_binary_bitmap(image):
    pixels = list(image.getdata())
    binary_pixels = [1 if pixel < 128 else 0 for pixel in pixels]  # Convert to 0 or 1
    binary_string = ''.join(map(str, binary_pixels))
    hex_bitmap = hex(int(binary_string, 2))
    return hex_bitmap

def createImage():
    width, height = 250, 122
    i = create_blank_image(width, height)

    Im = ImageDraw.Draw(i)
    mf = ImageFont.truetype('/home/aidanbrowne2002/open-paper/fonts/ShortBaby-Mg2w.ttf', 25)
    Im.text((15, 15), "Hello", 0, font=mf)  # Use 0 for monochrome (black) color

    hex_bitmap = image_to_binary_bitmap(i)
    print(hex_bitmap)
    return hex_bitmap
