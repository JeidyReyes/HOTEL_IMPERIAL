from . import views
from django.urls import path
from .views import login, contacto

urlpatterns = [
    path('login/', login.as_view(), name="login"),
    path('contacto/', contacto.as_view(), name="contacto"),
]
