from django.forms.models import ALL_FIELDS
from mini.forms import MusicForm
from mini.models import Music
from django.shortcuts import redirect, render
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
    if request.POST:
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            album = form.cleaned_data.get('album')
            if album:
                musi_album = Album.objects.get_or_create(album)
                instance.album = musi_album
                instance.save()
            else:
                instance.save()
            return redirect('index')
    return render(request,'music.html',{'form': form})

def registerPage(request):
    context={}
    return render(request, 'accounts/registration.html', context)

def loginPage(request):
    context={}
    return render(request, 'accounts/login.html', context)

