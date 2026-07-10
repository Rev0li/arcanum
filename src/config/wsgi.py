"""Point d'entrée WSGI (gunicorn). Par défaut sur les réglages de production ;
`DJANGO_SETTINGS_MODULE` reste surchargeable par l'environnement."""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

application = get_wsgi_application()
