# update/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from core.models import Inventario, Productos
from datetime import datetime

@login_required
def updateViews(request):
    if request.method == 'POST':
        # Eliminar productos
        if 'delete' in request.POST:
            producto_id = request.POST['delete']
            producto = get_object_or_404(Productos, id=producto_id)
            inventario = Inventario.objects.filter(idproducto=producto)
            inventario.delete()  # Primero eliminamos el registro en Inventario
            producto.delete()    # Luego eliminamos el registro en Producto
            return redirect('actualizar')

        # Actualizar productos existentes
        for key, value in request.POST.items():
            if key.startswith('nombre_') and key != 'nombre_new':
                producto_id = key.split('_')[1]
                producto = get_object_or_404(Productos, id=producto_id)
                producto.nombre = value
                producto.descripcion = request.POST.get(f'descripcion_{producto_id}')
                producto.precio = request.POST.get(f'precio_{producto_id}')
                inventario = Inventario.objects.get(idproducto=producto)
                inventario.cantidad = request.POST.get(f'cantidad_{producto_id}')
                producto.save()
                inventario.save()
        
        # Crear nuevo producto
        if request.POST.get('nombre_new'):
            nuevo_producto = Productos(
                nombre=request.POST.get('nombre_new'),
                descripcion=request.POST.get('descripcion_new'),
                precio=request.POST.get('precio_new'),
            )
            nuevo_producto.save()
            nuevo_inventario = Inventario(
                idproducto=nuevo_producto,
                cantidad=request.POST.get('cantidad_new'),
                fechaactualizacion=datetime.now()  # Establecer fecha de actualización actual
            )
            nuevo_inventario.save()
        return redirect('actualizar')  # Redirigir a la misma página después de guardar

    inventario = Inventario.objects.all()
    return render(request, 'update.html', {'inventario': inventario})
