from django.utils.translation import ugettext_lazy as _
from django import forms
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field


class ComparerForm(forms.Form):
    first_image = forms.ImageField()
    second_image = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(ComparerForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('form', _('Compare')))
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-sm-4'
        self.helper.field_class = 'col-sm-8'
