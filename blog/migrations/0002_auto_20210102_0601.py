# Generated by Django 3.1.4 on 2021-01-02 06:01

from django.db import migrations
import streams.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.core.fields.StreamField([('full_richtext', streams.blocks.RichTextBlock())], blank=True, null=True),
        ),
    ]
