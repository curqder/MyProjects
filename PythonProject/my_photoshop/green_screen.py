"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: image, the background image
    :param figure_img: image, the image with green screen
    :return: the combined image
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel = figure_img.get_pixel(x, y)
            bg_pixel = background_img.get_pixel(x, y)
            bigger = max(pixel.red, pixel.blue)
            if pixel.green > bigger * 2:
                pixel.red = bg_pixel.red
                pixel.green = bg_pixel.green
                pixel.blue = bg_pixel.blue
    return figure_img


def main():
    """
    Take place the figure image's green pixel with background image's pixel
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
