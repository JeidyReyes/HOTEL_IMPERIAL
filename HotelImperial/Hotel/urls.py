from . import views
from django.urls import path
from .views import anuncio, anuncios, blogentrada, blog, home, nosotros

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('nosotros/', nosotros.as_view(), name="nosotros"),
    path('blog/', blog.as_view(), name="blog"), 
    path('blogentrada/<titulo>', blogentrada.as_view(), name="blogentrada"), 
    path('anuncios/', anuncios.as_view(), name="anuncios"), 
    path('anuncio/<titulo>', anuncio.as_view(), name="anuncio"), 
]