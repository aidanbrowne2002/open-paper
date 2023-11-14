def generate_checkerboard(width, height):
    bitmap = []

    for y in range(height):
        row = []
        for x in range(width):
            # XOR of x and y to create a checkerboard pattern
            pixel_value = 0xFF if (x // 8) % 2 == (y // 8) % 2 else 0x00
            row.append(pixel_value)

        # Convert the row to 16 bytes (representing 122 pixels)
        hex_row = [f'0x{format(byte, "02X")}' for byte in row]
        row_str = ','.join(hex_row)
        # Duplicate the row to represent 16 bytes
        row_str *= 16
        bitmap.append(row_str)

    return bitmap

def display_bitmap(bitmap):
    return bitmap

# Generate and display the checkerboard bitmap for a 250x122 display
def createImage():
    width = 250
    height = 122
    checkerboard_bitmap = generate_checkerboard(width, height)
    bitmap = display_bitmap(checkerboard_bitmap)
    return bitmap

# Call the function to create and display the image
createImage()
