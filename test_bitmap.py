from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def create_blank_image(width, height):
    return Image.new("L", (width, height), "white")  # "L" mode for monochrome images

def image_to_binary_bitmap(image):
    width, height = image.size
    pixels = list(image.getdata())

    binary_values = ['1' if pixel < 128 else '0' for pixel in pixels]
    binary_string = ''.join(binary_values)

    # Group the binary string into rows of 8 pixels, adding 8 zeros between rows
    grouped_binary = [binary_string[i:i + 8] + '00000000' for i in range(0, len(binary_string), 8)]

    # Ensure each row is represented by 16 bytes
    grouped_binary = [row + '00000000' for row in grouped_binary]

    # Convert each row to hex
    hex_values = [f'0X{int(group[::-1], 2):02X}' for group in grouped_binary[::-1]]

    hex_bitmap = ','.join(hex_val for hex_val in hex_values)
    return hex_bitmap

def createImage():
    width, height = 122, 250
    i = create_blank_image(width, height)

    Im = ImageDraw.Draw(i)
    mf = ImageFont.truetype('/home/aidanbrowne2002/open-paper/fonts/ShortBaby-Mg2w.ttf', 25)
    Im.text((15, 15), "", 0, font=mf)  # Use 0 for monochrome (black) color

    hex_bitmap = image_to_binary_bitmap(i)
    print(hex_bitmap)
    return hex_bitmap
