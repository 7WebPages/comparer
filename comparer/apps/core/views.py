from django.utils.translation import ugettext as _
from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
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

        first_image_score = Hash(first_image).ahash()
        second_image_score = Hash(second_image).ahash()

        data['first_image'] = {
            'image': first_image,
            'score': first_image_score,
            'score_decimal': int(first_image_score, base=2)
        }

        data['second_image'] = {
            'image': second_image,
            'score': second_image_score,
            'score_decimal': int(second_image_score, base=2)
        }

        diff = int(second_image_score, base=2) - int(first_image_score, base=2)
        diff = abs(diff)
        data['diff_score'] = diff 

        return self.render_to_response(data)
