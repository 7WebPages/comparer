from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from core.views import *


urlpatterns = patterns(
    '',
    url(
        r'^$',
        HomeView,
        name="home"
    ),
)
