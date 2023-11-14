from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def binary_to_hex(arr):
    hex_array = []

    for row in arr:
        binary_string = ''.join(map(str, row))
        decimal_value = int(binary_string, 2)
        hex_value = hex(decimal_value)
        hex_array.append(hex_value)

    return hex_array
def create_blank_image(width, height):
    return Image.new("L", (width, height), "white")  # "L" mode for monochrome images

def image_to_binary_bitmap(image):
    width, height = image.size
    pixels = list(image.getdata())
    for i in range(len(pixels)):
        if pixels[i] < 128:
            pixels[i] = 0
        else:
            pixels[i] = 1

    for i in range(0, len(pixels), 250):
        chunk = pixels[i:i + 250]
        #print(chunk)

    pixelarray = []
    for i in range(0, len(pixels), 8):
        pixelarray.append(pixels[i:i + 8])
    #print(pixelarray)

    hexarray = binary_to_hex(pixelarray)
    return hexarray
def createImage():
    width, height = 250, 122
    i = create_blank_image(width, height)

    Im = ImageDraw.Draw(i)
    mf = ImageFont.truetype('fonts/BlockStockRegular-A71p.ttf', 25)
    Im.text((15, 15), "Lov", 0, font=mf)  # Use 0 for monochrome (black) color

    hex_bitmap = str(image_to_binary_bitmap(i))
    return hex_bitmap