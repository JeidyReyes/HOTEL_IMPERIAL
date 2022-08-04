from turtle import title
from django.shortcuts import render
from django.views.generic.base import TemplateView
from.models import About
from.models import Room
from.models import Blog
from.models import Testimony

# Create your views here.
class home(TemplateView):
    template_name = 'hotel/index.html'
    def get(selt, request):
        about = About.objects.all()
        rooms = Room.objects.all()
        blog = Blog.objects.all()
        testimony = Testimony.objects.all()
        return render(request, selt.template_name, {'rooms': rooms, 'about': about, 'blog': blog, 'testimony': testimony})

class nosotros(TemplateView):
    template_name = 'hotel/Nosotros.html'
    def get(selt, request):
        about = About.objects.all()
        return render(request, selt.template_name, {'about': about})

class blog(TemplateView):
    template_name = 'hotel/Blog.html'
    def get(selt, request):
        blog = Blog.objects.all()
        return render(request, selt.template_name, {'blog': blog})

class blogentrada(TemplateView):
    template_name = 'hotel/Blog-entrada.html'
    def get(selt, request, titulo):
        blog = Blog.objects.filter(title = titulo)
        return render(request, selt.template_name, {'blog': blog})

class anuncios(TemplateView):
    template_name = 'hotel/Anuncios.html'
    def get(selt, request):
        room = Room.objects.all()
        return render(request, selt.template_name, {'room': room})

class anuncio(TemplateView):
    template_name = 'hotel/Anuncio.html'
    def get(selt, request, titulo):
        room = Room.objects.filter(title = titulo)
        return render(request, selt.template_name, {'room':room})