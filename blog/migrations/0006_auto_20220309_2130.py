# Generated by Django 3.2.12 on 2022-03-10 04:30

from django.db import migrations, models
import modelcluster.fields
import streams.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220306_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, help_text='A slug to identify posts by this category', max_length=255, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Blog Category',
                'verbose_name_plural': 'Blog Categories',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='blogdetailpage',
            name='content',
            field=wagtail.core.fields.StreamField([('full_richtext', streams.blocks.RichTextBlock()), ('image_block_extra', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_caption', wagtail.core.blocks.CharBlock(required=False)), ('alignment', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('width', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('10', '10%'), ('20', '20%'), ('30', '30%'), ('40', '40%'), ('50', '50%'), ('60', '60%'), ('70', '70%'), ('80', '80%'), ('90', '90%'), ('100', '100%')]))])), ('gif_embed_block', wagtail.core.blocks.StructBlock([('input_html', wagtail.core.blocks.RawHTMLBlock()), ('alignment', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('start', 'Left'), ('center', 'Center'), ('end', 'Right')])), ('width', wagtail.core.blocks.ChoiceBlock(blank=False, choices=[('10', '10%'), ('20', '20%'), ('30', '30%'), ('40', '40%'), ('50', '50%'), ('60', '60%'), ('70', '70%'), ('80', '80%'), ('90', '90%'), ('100', '100%')]))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogdetailpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.BlogCategory'),
        ),
    ]
