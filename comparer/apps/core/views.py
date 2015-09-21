from django.utils.translation import ugettext as _
from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic.edit import import FormView

from core.forms import ComparerForm


class HomeView(FormView):
    form_class = ComparerForm
    template_name = "home.html" 
