# Generated by Django 3.2.12 on 2022-03-17 06:10

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20220310_0902'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='blog.bloghomepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
