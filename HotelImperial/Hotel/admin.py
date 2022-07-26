from django.contrib import admin
from.models import Room

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
admin.site.register(Room, RoomAdmin)