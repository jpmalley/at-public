# Generated by Django 3.1.14 on 2022-02-02 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_auto_20201227_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedia',
            name='spotify',
            field=models.URLField(blank=True, help_text='Spotify URL', null=True),
        ),
    ]
