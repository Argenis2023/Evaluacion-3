from django.shortcuts import render

# Create your views here.

def createUsersViews(request):
    return render(request, 'CrearUsuario.html')