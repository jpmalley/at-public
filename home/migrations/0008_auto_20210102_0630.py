# Generated by Django 3.1.4 on 2021-01-02 06:30

from django.db import migrations, models
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210102_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='section_2_content',
            field=wagtail.core.fields.StreamField([('full_richtext', streams.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False))])), ('button', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('btn', 'Standard'), ('btn-outline', 'Outline')])), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='Page overrides URL if one is chosen.', required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_heading',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='section_2_subheading',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
