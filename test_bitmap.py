from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import numpy as np


def binary_to_hex(arr):
    hex_array = []

    for row in arr:
        binary_string = ''.join(map(str, row))
        decimal_value = int(binary_string, 2)
        hex_value = hex(decimal_value)[2:].zfill(2)  # Ensure 2 digits, with leading zeros
        hex_array.append('0x' + hex_value)

    return hex_array


def create_blank_image(width, height):
    return Image.new("L", (width, height), "white")  # "L" mode for monochrome images


def image_to_binary_bitmap(image):
    width, height = image.size
    pixels = list(image.getdata())
    #print (len(pixels))




    for i in range(len(pixels)):
        if pixels[i] > 128:
            pixels[i] = 1
        else:
            pixels[i] = 0

    pixels_array = np.array(pixels).reshape(128, 250)

    # Step 2: Transpose the array (250x128)
    transposed_array = pixels_array.T

    # Step 3: Flip the transposed array horizontally
    flipped_array = np.flip(transposed_array, axis=1)

    # Step 4: Flatten the flipped array
    flattened_array = flipped_array.flatten()

    # Now, flattened_array contains your desired result with a horizontal flip
    pixels = flattened_array

    for i in range(0, len(pixels), 122):
        chunk = pixels[i:i + 122]
        #print(chunk)

    pixelarray = []
    for i in range(0, len(pixels), 8):
        pixelarray.append(pixels[i:i + 8])

    hexarray = binary_to_hex(pixelarray)
    return hexarray


def createImage(city,temp, desc):
    width, height = 250, 128
    i = create_blank_image(width, height)

    Im = ImageDraw.Draw(i)
    mf = ImageFont.truetype('fonts/SwanseaBold-D0ox.ttf', 16)
    Im.text((5, 8), f"Place: {city}", 0, font=mf)  # Use 0 for monochrome (black) color
    Im.text((5, 40), f"Temperature: {temp} C", 0, font=mf)  # Use 0 for monochrome (black) color
    Im.text((5, 80), f"Weather: {desc}", 0, font=mf)  # Use 0 for monochrome (black) color
    i.show()
    hex_bitmap = ', '.join(image_to_binary_bitmap(i)) + ','
    for i in range(0, len(hex_bitmap), 96):
        chunk = hex_bitmap[i:i + 96]
        #print(chunk)
    return hex_bitmap

import requests
import logging


