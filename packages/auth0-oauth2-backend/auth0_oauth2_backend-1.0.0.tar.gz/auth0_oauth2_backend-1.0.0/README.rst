
Overview
--------

Usage
-----


1. Add this package to your project's requiremets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Add this project to extra pip requirements.


..  code-block:: yaml

  OPENEDX_EXTRA_PIP_REQUIREMENTS:
  - git+https://github.com/blend-ed/auth0-oauth2-backend.git


2. Configure your Open edX lms application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: python

  from tutor import hooks

  hooks.Filters.ENV_PATCHES.add_items(
      [
          (
              "openedx-common-settings",
              """
  AUTH0_DOMAIN = <YOUR_AUTH0_DOMAIN>
  AUTH0_AUDIENCE = <YOUR_AUTH0_AUDIENCE>
              """,
          ),
          (
              "lms-env",
              """
  THIRD_PARTY_AUTH_BACKENDS: ["auth0_oauth2.auth0.Auth0OAuth2","social_core.backends.google.GoogleOAuth2", "common.djangoapps.third_party_auth.saml.SAMLAuthBackend", "django.contrib.auth.backends.ModelBackend"]
  SOCIAL_AUTH_AUTH0_PLUGIN_FIELDS_STORED_IN_SESSION:
  - "auth_entry"
  ADDL_INSTALLED_APPS:
  - "auth0_oauth2"
              """
          ),
          (
              "common-env-features",
              """
  ENABLE_THIRD_PARTY_AUTH: true
              """
          )
      ]
  )

3. Configure your Auth0 provider configurations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: screenshots/details.png
   :alt: Initial details section
   :align: center

.. image:: screenshots/options.png
   :alt: Options section
   :align: center

.. image:: screenshots/secrets.png
   :alt: Secrets section
   :align: center