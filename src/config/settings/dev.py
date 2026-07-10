"""Réglages de développement local : permissifs, aucune variable requise."""

import os

from .base import *  # noqa: F403

DEBUG = True

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "dev-insecure-ne-jamais-utiliser-en-production",
)

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

INTERNAL_IPS = ["127.0.0.1"]
