"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return: mirror-reflected image
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            b1_pixel = b_img.get_pixel(x, y)
            b2_pixel = b_img.get_pixel(x, b_img.height-y-1)
            b1_pixel.red = pixel.red
            b1_pixel.green = pixel.green
            b1_pixel.blue = pixel.blue
            b2_pixel.red = pixel.red
            b2_pixel.green = pixel.green
            b2_pixel.blue = pixel.blue
    return b_img


def main():
    """
    Create a blank image, draw it with original one's pixel
    the mirror pixel's y = b_img.height-y-1
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
