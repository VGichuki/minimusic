from mini.models import Music
from django.shortcuts import render
from django.http import HttpResponse
from .models import Music,Album

# Create your views here.
def home(request):
    music= Music.objects.all()
    return render(request, 'index.html', {'music': music})
