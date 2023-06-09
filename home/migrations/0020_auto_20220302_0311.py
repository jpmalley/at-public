# Generated by Django 3.1.14 on 2022-03-02 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('home', '0019_auto_20220302_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='cta_link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='CTA Button Page'),
        ),
    ]
