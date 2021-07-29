from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import Music, Album, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#Add forms here
class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields =['title', 'artist','audio_file','image']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')