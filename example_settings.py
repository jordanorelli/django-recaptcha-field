# Add these to your Django project's settings.py file to configure the
# reCAPTCHA fields.

# These two are required:
RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_PUBLIC_KEY = ''

# This one is optional.  It allows you to customize the error messages the
# user sees.
RECAPTCHA_ERROR_MESSAGES = {
    # We weren't able to verify the private key.
    'invalid-site-private-key': '',

    # The challenge parameter of the verify script was incorrect.
    'invalid-request-cookie': '',

    # The CAPTCHA solution was incorrect.
    'incorrect-captcha-sol': '',

    # reCAPTCHA never returns this error code. A plugin should manually return
    # this code in the unlikely event that it is unable to contact the
    # reCAPTCHA verify server.
    'recaptcha-not-reachable': '',
}

