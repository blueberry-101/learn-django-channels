from django.urls import path
from myapp.consumers import MyAWSconsumer,MyWSconsumer

websocket_urlpatterns = [
    path("ws/gwc/<str:group_name>/",MyWSconsumer.as_asgi(),name="gwc"),
    path("ws/gawc/<str:group_name>/",MyAWSconsumer.as_asgi(),name="gawc"),
]