from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def join_room(request: HttpRequest) -> HttpResponse:
    return render(request, 'chat/join_room.html')
