from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message, Room

@login_required
def rooms(request):
    rooms=Room.objects.all()
    context={'rooms':rooms}
    return render (request,'room/room.html',context)

@login_required
def room_detail(request,slug):
    room=Room.objects.get(slug=slug)
    messages=Message.objects.filter(room=room)[0:25]
    context={'room':room,'messages':messages}
    return render (request,'room/room_details.html',context)