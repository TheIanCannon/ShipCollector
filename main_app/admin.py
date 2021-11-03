from django.contrib import admin
from .models import Ship, Resupply, Photo

# Register your models here.
admin.site.register(Ship)
admin.site.register(Resupply)
admin.site.register(Photo)