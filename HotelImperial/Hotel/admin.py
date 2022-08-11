from django.contrib import admin
from.models import Room, Reservation, About, Blog,Testimony

# Register your models here.
class Admin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    
admin.site.register(Room, Admin)
admin.site.register(About, Admin)
admin.site.register(Blog, Admin)
admin.site.register(Testimony, Admin)
admin.site.register(Reservation)