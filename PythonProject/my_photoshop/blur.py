"""
File: blur.py
Name: 楊翔竣 Jim Yang
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""


from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the original image
    :return: img, the blurred image
    This function make image blurred
    """
    old_image = img
    blurred = SimpleImage.blank(old_image.width, old_image.height)
    for y in range(old_image.height):
        for x in range(old_image.width):
            count = 0
            sum_r = 0
            sum_g = 0
            sum_b = 0
            for i in range(-1, 2, 1):  # 1step, i= -1,0,1
                for j in range(-1, 2, 1):  # 1step, j = -1,0,1
                    pixel_x = x + j   # neighbor pixel
                    pixel_y = y + j   # neighbor pixel
                    if 0 <= pixel_x < old_image.width:
                        if 0 <= pixel_y < old_image.height:
                            pixel = old_image.get_pixel(pixel_x, pixel_y)
                            count += 1
                            sum_r += pixel.red
                            sum_g += pixel.green
                            sum_b += pixel.blue
            new_pixel = blurred.get_pixel(x, y)
            new_pixel.red = sum_r / count
            new_pixel.green = sum_g / count
            new_pixel.blue = sum_b / count
    return blurred


def main():
    """
    Use 4 for loops to find neighbors,
    and make new image's RGB values by neighbors' average
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
