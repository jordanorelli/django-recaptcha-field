from django import forms
from captchaform import CaptchaField

class CaptchaForm(forms.Form):
    captcha_field = CaptchaField()
