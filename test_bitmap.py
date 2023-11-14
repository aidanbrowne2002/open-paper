def generate_checkerboard(width, height):
    bitmap = []

    for y in range(height):
        row = []
        for x in range(width):
            if (x // 8) % 2 == (y // 8) % 2:
                row.append("0XFF")
            else:
                row.append("0X00")
        bitmap.append(','.join(row) + ',')

    return bitmap


def print_bitmap(bitmap):
    for row in bitmap:
        print(row)


width = 250
height = 122

bitmap = generate_checkerboard(width, height)
print_bitmap(bitmap)
def createImage():
    width = 250
    height = 122

    bitmap = generate_checkerboard(width, height)
    print_bitmap(bitmap)
    return bitmap