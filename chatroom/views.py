from django.shortcuts import render, redirect
from chatroom import forms as room_form
from chatroom import models as chatroom_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

@login_required(login_url='login')
def MyRooms(request):

    rooms = chatroom_model.Room.objects.filter(rcreated_by=request.user)
    context={
        "rooms":rooms
    }
    return render(request, "chatroom/rooms.html", context)

def AllRooms(request):
    rooms = chatroom_model.Room.objects.all()
    context={
        "rooms":rooms
    }
    return render(request, "chatroom/rooms.html", context)

@login_required(login_url='login')
def CreateRoom(request):
    form = room_form.CreateroomForm()

    if request.method == "POST":
        form = room_form.CreateroomForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.rcreated_by=request.user
            form.save()
            form.instance.ruser.add(request.user)
            return redirect('myroom')

    context = {
        'form':form
    }

    return render(request, 'chatroom/createroom.html', context)

@login_required(login_url='login')
def joinroom(request, rslug):
    try:
        room = chatroom_model.Room.objects.get(rslug=rslug)
        room.ruser.add(request.user)
        return redirect('chat', room.rslug)
    except Exception as e:
        messaage.error(request, "Room not find")
        return redirect('room')

@login_required(login_url='login')
def joinedroom(request):

    rooms = chatroom_model.Room.objects.filter(ruser=request.user)

    context = {
        'rooms':rooms
    }
    return render(request, 'chatroom/rooms.html', context)

@login_required(login_url='login')
def chat(request, rslug):
    room = chatroom_model.Room.objects.get(rslug=rslug)
    messages = chatroom_model.Message.objects.filter(room=room)[0:25]
    context={
        'room':room,
        'messages':messages
    }
    return render(request, 'chatroom/chat.html', context)

def rooomsearch(request):
    query = request.GET.get('q')
    rooms = chatroom_model.Room.objects.filter(Q(rname__icontains=query) | Q(rcollege__college__icontains=query) | Q(rcourse__course__icontains=query))
    context = {
        'rooms':rooms
    }
    return render(request, 'chatroom/rooms.html', context)