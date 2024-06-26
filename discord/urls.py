from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("room/<str:room_id>/", views.room, name="room"),
    path("create_room", views.createRoom, name="create_room")
]
