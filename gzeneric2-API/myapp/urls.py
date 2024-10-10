from django.urls import path
from myapp import views

urlpatterns = [
    path('chatroom/<str:groupname>/',views.chatroom,name="chatroom"),

]