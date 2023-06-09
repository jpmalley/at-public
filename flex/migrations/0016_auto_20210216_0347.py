# Generated by Django 3.1.5 on 2021-02-16 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0015_presspage_carousel_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='flexpage',
            name='header_image_position',
            field=models.CharField(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom')], default='center', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='presspage',
            name='header_image_position',
            field=models.CharField(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom')], default='center', max_length=6, null=True),
        ),
    ]
