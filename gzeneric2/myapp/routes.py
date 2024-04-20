from django.urls import path
from myapp.consumers import MyAWSconsumer,MyWSconsumer

websocket_urlpatterns = [
    path("ws/gwc/",MyWSconsumer.as_asgi(),name="gwc"),
    path("ws/gawc/",MyAWSconsumer.as_asgi(),name="gawc"),
]