from django import forms
from captchaform import CaptchaField

class ContactRequestForm(forms.Form):
    captcha_field = CaptchaField()
