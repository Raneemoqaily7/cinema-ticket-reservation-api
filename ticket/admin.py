from django.contrib import admin
from .models import Reservation ,Movie,Guest ,Review

# Register your models here.
admin.site.register(Reservation)
admin.site.register(Movie)
admin.site.register(Guest)
admin.site.register(Review)