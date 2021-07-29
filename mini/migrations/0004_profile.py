# Generated by Django 3.2.5 on 2021-07-29 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0003_alter_music_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('bio', models.TextField(blank=True, default='No bio', max_length=300)),
                ('profile_pic', models.ImageField(default='default.png', upload_to='images/')),
                ('contact', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
