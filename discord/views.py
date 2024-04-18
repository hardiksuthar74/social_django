from django.http import HttpResponse
from django.shortcuts import render
from .models import Room
from .forms import RoomForm


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "discord/home.html", context)


def find_room_by_id(id):
    room = Room.objects.get(id=id)
    return room


def room(request, room_id):
    room = find_room_by_id(room_id)
    context = {"room": room}
    return render(request, "discord/room.html", context)


def createRoom(request):
    if request.method == 'GET':
        form = RoomForm()
        context = {"form": form}
        return render(request, 'discord/room_form.html', context)
    elif request.method == "POST":
        pass
