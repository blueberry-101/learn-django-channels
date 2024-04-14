"""
ASGI config for gs4 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

#channels routing
from channels.routing import URLRouter,ProtocolTypeRouter
from myapp.routes import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs4.settings')

asgi_application = get_asgi_application()


application = ProtocolTypeRouter({
    "http": asgi_application,
    "websocket": URLRouter(
        websocket_urlpatterns
    )
})