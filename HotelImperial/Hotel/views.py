from datetime import datetime, timedelta
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from.models import About,Room,Blog,Testimony,Reservation
from django.contrib.auth import logout, authenticate, login as auth_login
from.forms import SignUpForm, SignipForm
from.models import Reservation

# Create your views here.

def login(request):
    if request.method=="POST":
        form=SignipForm(request,data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            user=authenticate(request,username=nombre, password=contra)
            if user is not None:
                auth_login(request,user)
                return redirect('home')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.success(request, "Informacion incorrecta")
    form = SignipForm
    return render(request, 'hotel/Login.html',{'form':form})

class registrar(TemplateView):
    template_name = 'hotel/Registrar.html'
    def get(selt, request):
        form = SignUpForm
        return render(request, selt.template_name,{'form':form})
    def post(selt, request):
        form= SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, selt.template_name, {'form':form})
def cerrar_sesion(request):
    logout(request)
    return redirect('home')
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
        fec = datetime.today()+timedelta(days=1)
        fecha = fec.strftime('%Y-%m-%d')
        room = Room.objects.filter(title = titulo)
        return render(request, selt.template_name,{'room':room, 'fecha':fecha})
    def post(selt, request, titulo):
        room = Room.objects.filter(title = titulo)
        fec = datetime.today()+timedelta(days=1)
        fecha = fec.strftime('%Y-%m-%d')
        if request.method=="POST":
            date=request.POST["date"]
            reser = Reservation.objects.filter(room=titulo, date=date)
            if reser.exists():
                messages.warning(request, "Fecha de reservacion no disponible")
                return render(request, selt.template_name,{'room':room, 'fecha':fecha })
            else: 
                user =request.POST["user"]
                client=request.POST["client"]
                email=request.POST["email"]
                reservacion = Reservation()
                reservacion.date=date
                reservacion.user= user
                reservacion.cliente=client
                reservacion.mail=email
                reservacion.room= titulo
                reservacion.save()
                messages.success(request, "Reservacion exitosa")
                return render(request, selt.template_name,{'room':room, 'fecha':fecha })
        else:
            return render(request, selt.template_name,{'room':room })

class reservacion(TemplateView):
    template_name = 'hotel/Reservaciones.html'
    def get(selt, request):
        reser = Reservation.objects.all()
        return render(request, selt.template_name, {'reser': reser})
    
class misreservacion(TemplateView):
    template_name = 'hotel/MisReservaciones.html'
    def get(selt, request, id):
        F_reser = Reservation.objects.filter(id = id)
        if F_reser.exists():
            F_reser.delete()
            messages.success(request, "Eliminacion exitosa")
        reser = Reservation.objects.all()
        return render(request, selt.template_name, {'reser': reser, 'Freser': F_reser})
        