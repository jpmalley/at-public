# Generated by Django 3.1.14 on 2022-02-28 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20220228_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='content_1_text_position',
            field=models.CharField(choices=[('left', 'Left'), ('right', 'right')], default='left', max_length=6, null=True),
        ),
    ]
