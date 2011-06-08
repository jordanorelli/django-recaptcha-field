from django.conf import settings

error_messages = {
    # We weren't able to verify the private key.
    'invalid-site-private-key': 'Invalid site private key.',

    # The challenge parameter of the verify script was incorrect.
    'invalid-request-cookie': 'Invalid request cookie.',

    # The CAPTCHA solution was incorrect.
    'incorrect-captcha-sol': 'Incorrect captcha solution.',

    # reCAPTCHA never returns this error code. A plugin should manually return
    # this code in the unlikely event that it is unable to contact the
    # reCAPTCHA verify server.
    'recaptcha-not-reachable': 'reCaptcha unreachable.',
}

def get_public_key():
    if not hasattr(settings, 'RECAPTCHA_PUBLIC_KEY'):
        raise Exception("Unable to determine reCaptcha public key.  Please "
                        "set RECAPTCHA_PUBLIC_KEY in your Django settings "
                        "module.")
    return settings.RECAPTCHA_PUBLIC_KEY

def get_private_key():
    if not hasattr(settings, 'RECAPTCHA_PRIVATE_KEY'):
        raise Exception("Unable to determine reCaptcha public key.  Please "
                        "set RECAPTCHA_PUBLIC_KEY in your Django settings "
                        "module.")
    return settings.RECAPTCHA_PRIVATE_KEY

def get_error_message(error_code):

    error_message = None
    if hasattr(settings, 'RECAPTCHA_ERROR_MESSAGES'):
        error_message = settings.RECAPTCHA_ERROR_MESSAGES.get(error_code)
    if error_message:
        return error_message

    return error_messages.get(error_code)
