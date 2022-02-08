from django.urls import path

from .views import join_room

app_name='chat'
urlpatterns = [
    path('room-join/', join_room, name='room_join')
]

