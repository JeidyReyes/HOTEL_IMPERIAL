from django.shortcuts import render
from.models import About
from.models import Room

# Create your views here.
def home(request):
    about = About.objects.all()
    rooms = Room.objects.all()
    return render(request, "hotel/index.html", {'rooms' : rooms, 'about' : about})