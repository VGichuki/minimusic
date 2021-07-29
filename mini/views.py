from django.forms.models import ALL_FIELDS
from mini.forms import MusicForm
from mini.models import Music
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Music,Album, Profile
from .forms import MusicForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    music= Music.objects.all()
    music_list = list(Music.objects.all().values())
    return render(request, 'index.html', {'music': music, 'music_list': music_list})

@login_required(login_url='login')
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
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
    context={'form': form}
    return render(request, 'accounts/registration.html', context)
    
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username =request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
            
        context={}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



