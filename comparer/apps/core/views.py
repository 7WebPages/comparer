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

        data['first_image'] = first_image
        data['second_image'] = second_image

        data['first_image_score'] = Hash(first_image).ahash()
        data['second_image_score'] = Hash(second_image).ahash()

        data['diff_score'] = 1 

        return self.render_to_response(data)
