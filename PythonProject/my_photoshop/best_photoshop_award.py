"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


THRESHOLD = 1.55
BLACK = 45


def main():
    """
    Because I have never gone skydiving, so l pretend to make dream come true.
    """
    fig = SimpleImage('image_contest/jim.jpg')
    bg = SimpleImage('image_contest/jpg.jpg')
    bg.make_as_big_as(fig)
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    """
    :param fig: image, the figure image
    :param bg: image, the background image
    :return: the combined image
    """
    for x in range(fig.width):
        for y in range(fig.height):
            pixel = fig.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue)//3
            bg_pixel = bg.get_pixel(x, y)
            total = pixel.red + pixel.green + pixel.blue
            if pixel.red > avg * THRESHOLD and total > BLACK:
                pixel.red = bg_pixel.red
                pixel.green = bg_pixel.green
                pixel.blue = bg_pixel.blue
    return fig



if __name__ == '__main__':
    main()
