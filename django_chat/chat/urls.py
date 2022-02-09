from django.urls import path

from .views import join_room, room

app_name = 'chat'
urlpatterns = [
    path('room-join/', join_room, name='room_join'),
    path('<str:room_name>/', room, name='room'),
]
