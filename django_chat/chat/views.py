from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def join_room(request: HttpRequest) -> HttpResponse:
    return render(request, 'chat/join_room.html')


def room(request: HttpRequest, room_name: str) -> HttpResponse:
    context = {'room_name': room_name}
    return render(request, 'chat/room.html', context)
