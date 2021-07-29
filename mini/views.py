from mini.forms import MusicForm
from mini.models import Music
from django.shortcuts import render
from django.http import HttpResponse
from .models import Music,Album
from .forms import MusicForm

# Create your views here.
def home(request):
    music= Music.objects.all()
    music_list = list(Music.objects.all().values())
    return render(request, 'index.html', {'music': music, 'music_list': music_list})

def newMusic(request):
    form = MusicForm()
    return render(request,'music.html',{'form': form})

