# Generated by Django 3.1.14 on 2022-01-05 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0022_auto_20220104_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programpage',
            name='program_price',
            field=models.DecimalField(decimal_places=2, default=1000.0, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='webinarpage',
            name='custom_title',
            field=models.CharField(blank=True, default='How to Advocate for Yourself by Setting Boundaries', max_length=100, null=True),
        ),
    ]
