import os
from django.core.exceptions import ValidationError
from mutagen.mp3 import MP3

#Create validators here
def validate_audio(file):
    try:
        audio = MP3(file)
        if not audio :
            raise TypeError()
        first_file_check =True
    except Exception as e:
        first_file_check=False
    if not first_file_check:
        raise ValidationError('Unauthorized file')
    valid_file_extension =('.mp3')
    extension =os.path.splitext(file.name)[1]
    if extension.lower() not in valid_file_extension:
        raise ValidationError('Unauthorized file')