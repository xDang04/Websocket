"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import URLRouter, ProtocolTypeRouter
from chat.routing import wsPattern

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

http_response_app = get_asgi_application()

application = ProtocolTypeRouter(
    {"http": http_response_app, "websocket":URLRouter(wsPattern)}
)