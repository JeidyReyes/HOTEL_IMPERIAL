from django.shortcuts import render
from.models import About
from.models import Room
from.models import Blog

# Create your views here.
def home(request):
    about = About.objects.all()
    rooms = Room.objects.all()
    blog = Blog.objects.all()
    return render(request, "hotel/index.html", {'rooms' : rooms, 'about' : about, 'blog' : blog})

