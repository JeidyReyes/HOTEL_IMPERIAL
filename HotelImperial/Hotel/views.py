from django.shortcuts import render
from.models import About
from.models import Room
from.models import Blog
from.models import Testimony

# Create your views here.


def home(request):
    about = About.objects.all()
    rooms = Room.objects.all()
    blog = Blog.objects.all()
    testimony = Testimony.objects.all()
    return render(request, "hotel/index.html", {'rooms': rooms, 'about': about, 'blog': blog, 'testimony': testimony})

def nosotros(request):
    about = About.objects.all()
    return render(request, "hotel/Nosotros.html", {'about': about})

def blog(request):
    blog = Blog.objects.all()
    return render(request, "hotel/Blog.html", {'blog': blog})

def blogentrada(request):
    blog = Blog.objects.all()
    return render(request, "hotel/Blog-entrada.html", {'blog': blog})
 