import os

from django.core.asgi import get_asgi_application

# add routes for websocket
from channels.routing import URLRouter,ProtocolTypeRouter
from myapp.routes import websocket_urlpatterns
##

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs3.settings')

asgi_application = get_asgi_application()

application = ProtocolTypeRouter({
    "http":asgi_application,
    "websocket": URLRouter(
        websocket_urlpatterns
    )
})