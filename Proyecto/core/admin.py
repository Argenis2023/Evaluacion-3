from django.contrib import admin
from .models import Inventario,Productos,InventarioView

# Register your models here.

admin.site.register(Inventario)
admin.site.register(Productos)