# Generated by Django 3.2.5 on 2021-07-29 13:16

from django.db import migrations, models
import mini.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='music',
            name='audio_file',
            field=models.FileField(upload_to='musics', validators=[mini.validators.validate_audio]),
        ),
    ]
