# Generated by Django 3.1.5 on 2021-01-17 23:26

from django.db import migrations
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0012_auto_20210117_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='content',
            field=wagtail.core.fields.StreamField([('full_richtext', streams.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False))])), ('button', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('btn', 'Standard'), ('btn-outline', 'Outline')])), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='Page overrides URL if one is chosen.', required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])), ('headline', wagtail.core.blocks.StructBlock([('headline_text', wagtail.core.blocks.CharBlock(required=True))])), ('left_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False))])), ('image_row', wagtail.core.blocks.StructBlock([('image_1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_1_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_2_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_3', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_3_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_4', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_4_caption', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presspage',
            name='bottom_content',
            field=wagtail.core.fields.StreamField([('full_richtext', streams.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False))])), ('button', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('btn', 'Standard'), ('btn-outline', 'Outline')])), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='Page overrides URL if one is chosen.', required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])), ('headline', wagtail.core.blocks.StructBlock([('headline_text', wagtail.core.blocks.CharBlock(required=True))])), ('left_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False))])), ('image_row', wagtail.core.blocks.StructBlock([('image_1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_1_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_2_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_3', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_3_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_4', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_4_caption', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='presspage',
            name='top_content',
            field=wagtail.core.fields.StreamField([('full_richtext', streams.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False))])), ('button', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('btn', 'Standard'), ('btn-outline', 'Outline')])), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='Page overrides URL if one is chosen.', required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])), ('headline', wagtail.core.blocks.StructBlock([('headline_text', wagtail.core.blocks.CharBlock(required=True))])), ('left_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False))])), ('image_row', wagtail.core.blocks.StructBlock([('image_1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_1_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_2_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_3', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_3_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_4', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_4_caption', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, null=True),
        ),
    ]
