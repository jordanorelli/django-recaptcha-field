from django import forms
from django.core.exceptions import ValidationError
from widgets import CaptchaWidget
from recaptcha.client import captcha
from utils import get_private_key
from utils import get_error_message

class CaptchaField(forms.Field):
    widget = CaptchaWidget

    def __init__(self, *args, **kwargs):
        if kwargs.has_key('widget') and kwargs['widget'] != CaptchaWidget:
            raise Exception('Overriding the captcha widget is not supported.')
        super(self.__class__, self).__init__(*args, **kwargs)

    def clean(self, value):
        try:
            captcha_response = captcha.submit(
                value.get('recaptcha_challenge_field'),
                value.get('recaptcha_response_field'),
                get_private_key(),
                '', # remote user's IP address.  See footnotes.
            )
        except Exception: # this is probably bad.
            error_message = get_error_message('recaptcha-not-reachable')
            raise ValidationError(error_message)

        if not captcha_response.is_valid:
            error_message = get_error_message(captcha_response.error_code)
            raise ValidationError(error_message)

        return value

################################################################################
#                                                                              #
# Footnotes                                                                    #
# ---------------------------------------------------------------------------- #
#                                                                              #
# As of writing, the remote user's IP address does not appear to be checked by #
# the reCaptcha service.  I tested both valid and invalid IP addresses as well #
# as an empty string.  Even though the input parameter is required by the      #
# recaptcha client library, there is no documentation on error codes involving #
# invalid remote user IPs.  An empty string is included to satisfy the client  #
# library requirements.                                                        #
#                                                                              #
################################################################################
