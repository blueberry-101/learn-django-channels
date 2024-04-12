import os

from django.core.asgi import get_asgi_application

# routing for channels
from channels.routing import URLRouter,ProtocolTypeRouter
from myapp.routes import websocket_urlpatterns
####


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gs2.settings')

django_asgi_app = get_asgi_application()


# add code to handle websocket urls patterns
application = ProtocolTypeRouter({
    "http":django_asgi_app,
    "websocket": URLRouter(
        websocket_urlpatterns
    )
})
###