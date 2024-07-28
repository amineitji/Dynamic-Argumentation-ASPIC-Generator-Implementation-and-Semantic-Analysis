# aspic_generator/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'aspic_generator/index.html')
