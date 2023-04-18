# Generated by Django 3.1.5 on 2021-02-16 05:33

from django.db import migrations, models
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_auto_20210208_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribepage',
            name='header_image_position',
            field=models.CharField(choices=[('top', 'Top'), ('center', 'Center'), ('bottom', 'Bottom')], default='center', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='subscribepage',
            name='thank_you_text',
            field=wagtail.core.fields.StreamField([('full_richtext', streams.blocks.RichTextBlock()), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False))])), ('button', wagtail.core.blocks.StructBlock([('button_text', wagtail.core.blocks.CharBlock(required=True)), ('button_style', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('btn', 'Standard'), ('btn-outline', 'Outline')])), ('button_page', wagtail.core.blocks.PageChooserBlock(help_text='Page overrides URL if one is chosen.', required=False)), ('button_url', wagtail.core.blocks.URLBlock(required=False))])), ('headline', wagtail.core.blocks.StructBlock([('headline_text', wagtail.core.blocks.CharBlock(required=True))])), ('left_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False)), ('content', wagtail.core.blocks.RichTextBlock(required=False))])), ('image_row', wagtail.core.blocks.StructBlock([('image_1', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_1_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_2', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_2_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_3', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_3_caption', wagtail.core.blocks.CharBlock(required=False)), ('image_4', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_4_caption', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, null=True),
        ),
    ]
