"""Authomatic Oauth configuration file

Pull secret ids and keys from environment variables set in .env
"""

import os

from authomatic import Authomatic
from authomatic.providers import oauth2

OAUTH_CONFIG = {
    "Facebook": {  # This name is arbitrary but is easier if it matches oauth provider name
        "id": 1,  # These id numbers are arbitrary
        "class_": oauth2.Facebook,  # Use authomatic's Facebook handshake
        "consumer_key": os.getenv("FACEBOOK_ID"),
        "consumer_secret": os.getenv("FACEBOOK_SECRET"),
    },
    "Google": {
        "id": 1,  # These id numbers are arbitrary
        "class_": oauth2.Google,
        "consumer_key": os.getenv("GOOGLE_ID"),
        "consumer_secret": os.getenv("GOOGLE_SECRET"),
        # Google requires a scope be specified to work properly
        "scope": ["profile", "email"],
    },
    "GitHub": {
        "id": 3,  # These id numbers are arbitrary
        "class_": oauth2.GitHub,  # Use authomatic's GitHub handshake
        # GitHub requires a special header to work properly
        "access_headers": {"User-Agent": "YOUR_APP_NAME"},  # Fill in with your app name
        "consumer_key": os.getenv("GITHUB_ID"),
        "consumer_secret": os.getenv("GITHUB_SECRET"),
    },
}

# Instantiate Authomatic.
authomatic = Authomatic(
    OAUTH_CONFIG,
    os.getenv("AUTHOMATIC_SECRET"),
    report_errors=True,  # Set to False in production
)
