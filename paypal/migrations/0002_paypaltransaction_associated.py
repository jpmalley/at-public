# Generated by Django 3.1.5 on 2021-09-02 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paypal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paypaltransaction',
            name='associated',
            field=models.BooleanField(default=False),
        ),
    ]
