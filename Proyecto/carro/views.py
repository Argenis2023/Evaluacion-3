from django.shortcuts import render

# Create your views here.


def carroViews(request):
    return render(request, 'carro.html')