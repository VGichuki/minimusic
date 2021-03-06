from mini.validators import validate_audio
from mini.helpers import get_audio_length
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=1000)
    artist = models.CharField(max_length=500)
    album = models.ForeignKey('Album',null=True, blank=True, on_delete=models.SET_NULL)
    time_length = models.DecimalField(max_digits=50,decimal_places=2,blank=True)
    audio_file = models.FileField(upload_to='musics', validators=[validate_audio])
    image= models.ImageField(upload_to='music_image/')

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        if not self.time_length:
            #Login for getting music length
            audio_length = get_audio_length(self.audio_file)
            self.time_length = audio_length
        return super().save(*args, **kwargs)

    

class Album(models.Model):
    name = models.CharField(max_length=1000)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=300, blank=True, default='No bio')
    profile_pic = models.ImageField(upload_to='images/', default='default.png')
    contact = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()




