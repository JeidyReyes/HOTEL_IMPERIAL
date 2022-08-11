from django.shortcuts import render, redirect
from django.views.generic import View
class contacto(View):
    template_name = 'core/contacto.html'
    def get(selt, request):
        return render(request, selt.template_name)
