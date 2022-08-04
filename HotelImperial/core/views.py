from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class login(TemplateView):
    template_name = 'core/Login.html'
    def get(selt, request):
        return render(request, selt.template_name)

class contacto(TemplateView):
    template_name = 'core/contacto.html'
    def get(selt, request):
        return render(request, selt.template_name)
