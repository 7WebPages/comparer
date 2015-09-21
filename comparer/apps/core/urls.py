from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from core.views import *


urlpatterns = patterns(
    '',
    url(
        r'^$',
        TemplateView.as_view(template_name='home.html'),
        name="home"
    ),
)
