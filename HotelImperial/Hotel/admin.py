from django.contrib import admin
from.models import Room
from.models import About

# Register your models here.
class Admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
admin.site.register(Room, Admin)
admin.site.register(About, Admin)