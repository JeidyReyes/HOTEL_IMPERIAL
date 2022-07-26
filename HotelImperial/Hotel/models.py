from django.db import models

# Create your models here.
class Room (models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    price = models.FloatField(verbose_name="Precio")
    image = models.ImageField(verbose_name="Imagen", upload_to= "rooms")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")

    class Meta:
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'
        ordering = ["-created"]
    def __str__(self):
        return self.title 