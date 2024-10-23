Overview
--------

This is a custom backend for Open edX that allows users to authenticate using Auth0. It also supports OTP login for users who have enabled it in their Auth0 account.

Usage
-----

1. Add this package to your project's requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add this project to your extra pip requirements.

.. code-block:: yaml

    OPENEDX_EXTRA_PIP_REQUIREMENTS:
      - git+https://github.com/blend-ed/auth0-oauth2-backend.git

2. Configure your Open edX LMS application
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from tutor import hooks

    hooks.Filters.ENV_PATCHES.add_items(
        [
            (
                "openedx-common-settings",
                """
                AUTH0_DOMAIN = "<YOUR_AUTH0_DOMAIN>"
                AUTH0_AUDIENCE = "<YOUR_AUTH0_AUDIENCE>"
                TPA_AUTOMATIC_LOGOUT_ENABLED = True
                """,
            ),
            (
                "lms-env",
                """
                THIRD_PARTY_AUTH_BACKENDS: [
                    "auth0_oauth2.auth0.Auth0OAuth2",
                    "social_core.backends.google.GoogleOAuth2",
                    "common.djangoapps.third_party_auth.saml.SAMLAuthBackend",
                    "django.contrib.auth.backends.ModelBackend"
                ]
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

This is the code to be placed in the other settings field:

.. code-block:: python

    {
      "DOMAIN": <Your Auth0 domain>,
      "DEFAULT_SCOPE": [
        "openid",
        "profile",
        "email"
      ]
    }

Images
------

.. image:: https://github.com/user-attachments/assets/37ab6f4f-5c43-4ece-b53e-b1102c4457c5
   :alt: Initial details section
   :align: center

.. image:: https://github.com/user-attachments/assets/0cd7911e-382d-4891-965c-69cfa7b0e4b0
   :alt: Options section
   :align: center

.. image:: https://github.com/user-attachments/assets/70361467-6fbb-40a7-ba2a-b7967a1b52f4
   :alt: Secrets section
   :align: center

4. Configure your Auth0 application in Auth0 dashboard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Go to your Auth0 dashboard
- Click on settings and then go to the advanced settings
- Add the logout URL of your Open edX instance in the allowed logout URLs

.. image:: https://github.com/user-attachments/assets/83714527-bada-44c3-a236-d2b8f1a32294
   :alt: Allowed logout URLs
   :align: center
