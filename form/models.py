from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from streams import blocks

class FormField(AbstractFormField):
    
    page = ParentalKey(
        'FormPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
        )

class FormPage(WagtailCaptchaEmailForm):

    template = "form/form_page.html"

    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"
    IMAGE_POSITION_CHOICES = [
        (TOP, "Top"),
        (CENTER, "Center"),
        (BOTTOM, "Bottom"),
    ]

    custom_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Page display title. Overwrites the default title.",
    )

    header_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    header_image_position = models.CharField(
        max_length=6, 
        blank=False, 
        null=True,
        choices=IMAGE_POSITION_CHOICES,
        default=CENTER,
    )

    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("image", blocks.ImageBlock()),
            ("button", blocks.ButtonBlock()),
            ("headline", blocks.HeadlineBlock()),
            ("left_image", blocks.LeftImageBlock()),
            ("image_row", blocks.ImageRowBlock()),
        ],
        null=True,
        blank=True
    )

    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("custom_title"),
        MultiFieldPanel([
            ImageChooserPanel("header_image"),
            FieldPanel("header_image_position"),
        ], heading="Header Image", classname="collapsible"),
        StreamFieldPanel("content"),
        InlinePanel("form_fields", label="Form Fields"),
        FieldPanel("thank_you_text"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("from_address", classname="col6"),
                FieldPanel("to_address", classname="col6")
            ]),
            FieldPanel("subject"),
        ], heading="Email Settings"),
    ]