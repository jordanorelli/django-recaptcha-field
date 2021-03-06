Makes adding reCAPTCHA fields to Django forms easy.

Installation:

First, make sure you have the [recaptcha-client](http://pypi.python.org/pypi/recaptcha-client) library installed:

    pip install recaptcha-client

(or)

    easy_install recaptcha-client


Once the library is installed, set your reCAPTCHA public and private keys in your Django project's settings.py file.  You will want to use the keys **RECAPTCHA_PUBLIC_KEY** and **RECAPTCHA_PRIVATE_KEY** for this.

The default error messages I wrote are pretty flavorless.  You can change these by creating a **RECAPTCHA_ERROR_MESSAGES** dictionary in your settings.py file.  The error message keys are as follows:

<dl>
  <dt>invalid-site-private-key</dt>
  <dd>We weren't able to verify the private key.</dd>
  <dt>invalid-request-cookie</dt>
  <dd>The challenge parameter of the verify script was incorrect.</dd>
  <dt>incorrect-captcha-sol</dt>
  <dd>The CAPTCHA solution was incorrect.</dd>
  <dt>recaptcha-not-reachable</dt>
  <dd>The Django server was unable to reach the reCAPTCHA server.</dd>
</dl>

This has been tested against recaptcha-client version 1.0.6 and Django 1.3.
