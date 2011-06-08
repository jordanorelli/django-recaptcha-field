from django import forms
from django.forms.util import flatatt
from django.utils.safestring import mark_safe
from recaptcha.client import captcha
from utils import get_public_key

class CaptchaWidget(forms.Widget):

    def value_from_datadict(self, data, files, name):
        return {
            'recaptcha_challenge_field': data.get('recaptcha_challenge_field'),
            'recaptcha_response_field': data.get('recaptcha_response_field'),
        }

    def render(self, *args, **kwargs):
        return captcha.displayhtml(get_public_key())
