# -*- coding: utf-8 -*-
import glob
import os

import numpy as np

from sklearn import linear_model
from itertools import combinations

from django.core.management.base import BaseCommand
from django.conf import settings

from core.hash_utils import Hash


class Command(BaseCommand):

    def handle(self, *args, **options):
        # basedir = os.path.join(settings.SITE_ROOT, 'comparer', 'apps', 'core', 'data', 'images')
        # scores = {}
        # for filename in glob.glob("%s/*.jpg" % basedir):
        #     key = os.path.basename(filename)
        #     hasher = Hash(filename)
        #     scores[key] = hasher.calc_scores()
        #
        # result = open(os.path.join(settings.SITE_ROOT, 'comparer', 'apps', 'core', 'data', 'result.csv'), 'w')
        # for img1, img2 in combinations(scores.keys(), 2):
        #     vector = []
        #     for s1, s2 in zip(scores[img1], scores[img2]):
        #         vector.append(Hash.calc_difference(s1[1], s2[1]))
        #     result.write('%s vs %s;%s\n' % (img1, img2, vector))

        classifier = linear_model.LogisticRegression()
        result = open(os.path.join(settings.SITE_ROOT, 'comparer', 'apps', 'core', 'data', 'result.csv'))
        test = []
        target = []
        for item in result.readlines():
            items = item.replace('\n', '').split(';')
            vector = map(int, items[1].replace('[', '').replace(']', '').split(','))
            v = 1 if items[2] else 0
            target.append(v)
            test.append(vector)
        test = np.array(test)
        target = np.array(target)
        classifier = classifier.fit(test, target)
        print classifier.intercept_
        print classifier.coef_