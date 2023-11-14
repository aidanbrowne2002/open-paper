def generate_checkerboard(width, height):
    bitmap = []

    for y in range(height):
        row = []
        for x in range(width):
            # XOR of x and y to create a checkerboard pattern
            pixel_value = 0xFF if (x // 8) % 2 == (y // 8) % 2 else 0x00
            row.append(pixel_value)

        # Convert the row to hexadecimal format
        hex_row = [f'0x{format(byte, "02X")}' for byte in row]
        row_str = ','.join(hex_row)
        bitmap.append(row_str)

    return bitmap

def display_bitmap(bitmap):
    for row in bitmap:
        print(row)
    return bitmap

# Generate and display the checkerboard bitmap for a 250x122 display
def createImage():
    width = 250
    height = 122
    checkerboard_bitmap = generate_checkerboard(width, height)
    bitmap = display_bitmap(checkerboard_bitmap)
    return bitmap
