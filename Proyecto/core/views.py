from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def homeView(request):
    return render(request, 'index.html')