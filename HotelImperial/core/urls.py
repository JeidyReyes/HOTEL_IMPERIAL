from . import views
from django.urls import path
from .views import contacto

urlpatterns = [
    path('contacto/', contacto.as_view(), name="contacto"),
]
