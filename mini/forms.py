from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import Music, Album

#Add forms here
class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields =['title', 'artist','audio_file','image']