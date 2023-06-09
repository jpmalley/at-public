# Generated by Django 3.1.14 on 2022-03-01 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0017_auto_20220301_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='stat_background_image',
        ),
        migrations.AddField(
            model_name='homepage',
            name='cta_headline',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='cta_link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='cta_link_text',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='cta_link_url',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='homepage',
            name='open_in_new_tab',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
