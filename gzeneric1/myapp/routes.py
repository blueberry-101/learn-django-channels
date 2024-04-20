from myapp.consumers import MyWSconsumer,MyAWSconsumer
from django.urls import path

websocket_urlpatterns = [
    path("ws/gsc/",MyWSconsumer.as_asgi(),name="gsyncc"),
    path("ws/gac/",MyAWSconsumer.as_asgi(),name="gasyncc")

]