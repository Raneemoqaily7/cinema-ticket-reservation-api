from django.contrib import admin
from .models import Reservation ,Movie,Guest

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Movie)
admin.site.register(Guest)