from django.core.urlresolvers import reverse
from django.utils import formats

from django_webtest import WebTest
from webtest import Upload
from model_mommy import mommy
from allauth.account.models import EmailAddress
