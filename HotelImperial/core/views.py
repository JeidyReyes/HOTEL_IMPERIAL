from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "core/Login.html")

def contacto(request):
    return render(request, "core/contacto.html")
