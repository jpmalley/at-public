# Generated by Django 3.2.12 on 2022-03-10 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogcategory_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
