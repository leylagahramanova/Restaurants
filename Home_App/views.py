from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
# Create your views here.

def home(request):
    restaurants=Articles.objects.all()
    return render(request, 'home.html', {'restaurants':restaurants})

def about(request):
    return render(request, 'about.html')