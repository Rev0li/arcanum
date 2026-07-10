"""Point d'entrée ASGI. Par défaut sur les réglages de production ;
`DJANGO_SETTINGS_MODULE` reste surchargeable par l'environnement."""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

application = get_asgi_application()
