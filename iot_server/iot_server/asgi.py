"""
ASGI config for iot_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import stream.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iot_server.settings')
django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket" : AuthMiddlewareStack(
        URLRouter(
            stream.routing.websocket_urlpatterns,
        )
    )
})