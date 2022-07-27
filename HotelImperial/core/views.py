from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return render(request, "core/Login.html")

def nosotros(request):
    return render(request, "core/Nosotros.html")