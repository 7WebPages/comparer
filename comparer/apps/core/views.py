# -*- coding: utf-8 -*-
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.generic.edit import FormView

from core.forms import ComparerForm
from core.hash_utils import Hash


class HomeView(FormView):
    form_class = ComparerForm
    template_name = "home.html"
    success_url = '/'

    def form_valid(self, form):
        data = self.get_context_data() 
        data['form'] = form

        first_image = form.cleaned_data['first_image']
        second_image = form.cleaned_data['second_image']

        first_image_url = self.save_image(first_image)
        second_image_url = self.save_image(second_image)

        first_image_hasher = Hash(first_image)
        second_image_hasher = Hash(second_image)

        first_image_score = first_image_hasher.ahash()
        second_image_score = second_image_hasher.ahash()

        s1 =  first_image_hasher.calc_scores()
        s2 = second_image_hasher.calc_scores()
        vector = []
        for h1, h2 in zip(s1, s2):
            vector.append(Hash.calc_difference(h1[1], h2[1]))
        data['is_duplicates'] = Hash.predict(vector)

        data['first_image'] = {
            'image': first_image_url,
            'score': first_image_score,
            'score_decimal': int(first_image_score, base=2)
        }

        data['second_image'] = {
            'image': second_image_url,
            'score': second_image_score,
            'score_decimal': int(second_image_score, base=2)
        }

        diff = 0
        for i in range(len(second_image_score)):
            if first_image_score[i] != second_image_score[i]:
                diff += 1
        data['diff_score'] = diff

        return self.render_to_response(data)

    def save_image(self, image):
        url = default_storage.save(image.name, ContentFile(image.read()))
        return url
