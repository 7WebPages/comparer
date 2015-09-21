from PIL import Image


class Hash(object):

    def __init__(self, image):
        self.image = Image.open(image)

    def ahash(self):
        im = self.image
        size = 16, 16

        # resize
        im = im.resize(size, Image.ANTIALIAS)

        # convert to greyscale
        #  L = R * 299/1000 + G * 587/1000 + B * 114/1000
        im = im.convert('L')

        # Calc average value of pixels
        pixels = list(im.getdata())
        average = sum(pixels) / len(pixels)

        result = ''
        for pixel in pixels:
            if pixel > average:
                result += '1'
            else:
                result += '0'

        return result
