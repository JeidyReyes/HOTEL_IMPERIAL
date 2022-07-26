from django.shortcuts import render
from.models import Room

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, "hotel/index.html", {'rooms' : rooms})