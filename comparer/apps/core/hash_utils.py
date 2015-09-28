# -*- coding: utf-8 -*-
import numpy

from sklearn import linear_model
from PIL import Image, ImageOps


class Hash(object):

    def __init__(self, image):
        if not isinstance(image, basestring):
            image.seek(0)
        self.image = Image.open(image)

    def prepare_image(self, crop_width_perc=0, crop_height_perc=0, fit_image=True):
        result = self.image

        # convert to grayscale
        result = result.convert('L')

        # crop image
        image_size = result.size
        width_crop_size = int(image_size[0] * crop_width_perc / 2) if crop_width_perc > 0 else 0
        height_crop_size = int(image_size[1] * crop_height_perc / 2) if crop_height_perc > 0 else 0
        if width_crop_size or height_crop_size:
            result = result.crop(
                (
                    width_crop_size,
                    height_crop_size,
                    image_size[0] - width_crop_size,
                    image_size[1] - height_crop_size
                )
            )

        # resize to 128x128 pixels
        resize_option = Image.ANTIALIAS
        if fit_image:
            return ImageOps.fit(result, (128, 128), resize_option)

        return result.resize((128, 128), resize_option)

    def ahash(self, img=None, hash_size=16):
        im = img or self.image
        im = im.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)
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

    def calc_scores(self):
        alg = (
            ('crop', 0, 0, 8, True),  # original fitted to 128x128
            ('crop', 0, 0.1, 8, True), # vertical 10% crop fitted to 128x128
            ('crop', 0.1, 0, 8, True), # horizontal 10% crop fitted to 128x128
            ('crop', 0.1, 0.1, 8, True), # vertical and horizontal 10% crop fitted to 128x128

            ('crop', 0, 0, 8, False),  # original resized to 128x128
            ('crop', 0, 0.1, 8, False), # vertical 10% crop resized to 128x128
            ('crop', 0.1, 0, 8, False), # horizontal 10% crop resized to 128x128
            ('crop', 0.1, 0.1, 8, False) # vertical and horizontal 10% crop resized to 128x128
        )
        scores = []
        for item in alg:
            if item[0] == 'crop':
                v, h, hash_size, fit_image = item[1:]
                name = '%s_%s_%s_%s_%s' % item
                value = self.ahash(
                    img=self.prepare_image(
                        crop_width_perc=v,
                        crop_height_perc=h,
                        fit_image=fit_image
                    ),
                    hash_size=hash_size
                )
                scores.append((name, value))
        return scores

    @classmethod
    def calc_difference(cls, h1, h2):
        diff = 0
        for a, b in zip(h1, h2):
            diff += int(a != b)
        return diff

    @classmethod
    def predict(cls, vector):
        coefs = numpy.array(
            [
                [
                    0.30346249,
                    -0.33800637,
                    -0.30347395,
                    -0.33800637,
                    0.05190433,
                    -0.20001436,
                    0.07453074,
                    0.29136006
                ]
            ]
        )
        classifier = linear_model.LogisticRegression()
        classifier.coef_ = coefs
        classifier.intercept_ = numpy.array([ 1.98375232])
        resutl = classifier.predict_proba(numpy.array(vector))
        match = resutl[:, 1] > resutl[:, 0]
        return match[0]
