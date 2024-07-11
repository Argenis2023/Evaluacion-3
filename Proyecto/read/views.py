from django.shortcuts import render
from core.models import InventarioView

def mostrar_inventario(request):
    inventario = InventarioView.objects.all()
    return render(request, 'read.html', {'inventario': inventario})