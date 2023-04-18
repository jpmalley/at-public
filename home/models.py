from pydoc import classname
from django.db import models
from django.shortcuts import render
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from streams import blocks

class IamList(Orderable):
    """List of descriptors on home page"""
    NONE = ""
    A = "a"
    AN = "an"
    THE = "the"
    ARTICLE_CHOICES = [
        (NONE, "none"),
        (A, "A"),
        (AN, "An"),
        (THE, "The")
    ]

    page = ParentalKey("home.HomePage", related_name="descriptors")
    article = models.CharField(
        max_length=4, 
        blank=False, 
        null=True,
        choices=ARTICLE_CHOICES,
        default=A,
    )
    descriptor = models.CharField(
        max_length=26,
        blank=False,
        null=True,
    )

    panels = [
        FieldPanel("article"),
        FieldPanel("descriptor"),
    ]

class TestimonialCarousel(Orderable):
    """Between 1 and 5 testimonials for the home page."""

    page = ParentalKey("home.HomePage", related_name="testimonials")
    testimonial_text = models.TextField(max_length=700, blank=False, null=True)
    testimonial_author = models.CharField(max_length=100, blank=False, null=True)

    panels = [
        FieldPanel("testimonial_text"),
        FieldPanel("testimonial_author"),
    ]

class HomePage(RoutablePageMixin, Page):
    """Home page model."""

    template = "home/home_page.html"
    max_count = 1

    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"
    DARK = "dark"
    LIGHT = "light"

    IMAGE_POSITION_CHOICES = [
        (TOP, "Top"),
        (CENTER, "Center"),
        (BOTTOM, "Bottom"),
    ]

    TEXT_POSITION_CHOICES = [
        (LEFT, "Left"),
        (RIGHT, "Right")
    ]

    TEXT_COLOR_CHOICES = [
        (DARK, "Dark"),
        (LIGHT, "Light")
    ]

    quote_1 = models.CharField(
        max_length=150, 
        blank=False, 
        null=True
    )
    
    quote_2 = models.CharField(
        max_length=150, 
        blank=False, 
        null=True
    )

    content_1 = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("image", blocks.ImageBlock()),
            ("button", blocks.ButtonBlock()),
            ("headline", blocks.HeadlineBlock()),
        ],
        null=True,
        blank=True
    )

    content_1_text_position = models.CharField(
        max_length=6, 
        blank=False, 
        null=True,
        choices=TEXT_POSITION_CHOICES,
        default=LEFT,
    )

    content_1_text_color = models.CharField(
        max_length=6, 
        blank=False, 
        null=True,
        choices=TEXT_COLOR_CHOICES,
        default=DARK,
    )

    content_1_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_2 = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("image", blocks.ImageBlock()),
            ("button", blocks.ButtonBlock()),
            ("headline", blocks.HeadlineBlock()),
        ],
        null=True,
        blank=True
    )

    content_2_text_position = models.CharField(
        max_length=6, 
        blank=False, 
        null=True,
        choices=TEXT_POSITION_CHOICES,
        default=LEFT,
    )

    content_2_text_color = models.CharField(
        max_length=6, 
        blank=False, 
        null=True,
        choices=TEXT_COLOR_CHOICES,
        default=DARK,
    )

    content_2_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_3 = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("image", blocks.ImageBlock()),
            ("button", blocks.ButtonBlock()),
            ("headline", blocks.HeadlineBlock()),
        ],
        null=True,
        blank=True
    )

    content_3_text_position = models.CharField(
        max_length=6, 
        blank=False, 
        null=True,
        choices=TEXT_POSITION_CHOICES,
        default=LEFT,
    )

    content_3_text_color = models.CharField(
        max_length=6, 
        blank=False, 
        null=True,
        choices=TEXT_COLOR_CHOICES,
        default=DARK,
    )

    content_3_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    cta_headline = models.CharField(
        max_length=150, 
        blank=False, 
        null=True
    )

    cta_link_text = models.CharField(
        max_length=32, 
        blank=False, 
        null=True
    )

    cta_link_url = models.CharField(
        max_length=500,
        blank=True,
    )

    cta_link_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        related_name="+",
        on_delete=models.SET_NULL,
        verbose_name="CTA Button Page"
    )

    # @property
    def cta_link(self):
        if self.cta_link_page:
            return self.cta_link_page.url
        elif self.cta_link_url:
            return self.cta_link_url
        return '#'

    open_in_new_tab = models.BooleanField(default=False, blank=True)

    testimonial_background_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel("descriptors", max_num=8, min_num=1, label="Descriptor"),
        ], heading="Hero Section", classname="collapsible"),
        MultiFieldPanel([
            StreamFieldPanel("content_1"),
            FieldRowPanel([
                FieldPanel("content_1_text_color", classname="col6"),
                FieldPanel("content_1_text_position", classname="col6")
            ]),
            ImageChooserPanel("content_1_background_image"),
        ], heading="Content Section 1", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel("quote_1"),
        ], heading="Quote Section 1", classname="collapsible"),
        MultiFieldPanel([
            StreamFieldPanel("content_2"),
            FieldRowPanel([
                FieldPanel("content_2_text_color", classname="col6"),
                FieldPanel("content_2_text_position", classname="col6")
            ]),
            ImageChooserPanel("content_2_background_image"),
        ], heading="Content Section 2", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel("quote_2"),
        ], heading="Quote Section 2", classname="collapsible"),
        MultiFieldPanel([
            StreamFieldPanel("content_3"),
            FieldRowPanel([
                FieldPanel("content_3_text_color", classname="col6"),
                FieldPanel("content_3_text_position", classname="col6")
            ]),
            ImageChooserPanel("content_3_background_image"),
        ], heading="Content Section 3", classname="collapsible"),
        MultiFieldPanel([
            FieldPanel("cta_headline", heading="CTA Headline"),
            FieldPanel("cta_link_text", heading="CTA Button Text"),
            FieldPanel("cta_link_url", heading="CTA Button URL"),
            PageChooserPanel("cta_link_page"),
            FieldPanel("open_in_new_tab"),
        ], heading="CTA Section", classname="collapsible"),
        MultiFieldPanel([
            InlinePanel("testimonials", max_num=6, min_num=1, label="Testimonial"),
            ImageChooserPanel("testimonial_background_image"),
        ], heading="Testimonial Section", classname="collapsible"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


    # @route(r'^subscribe/$')
    # def subscribe_page(self, request, *args, **kwargs):
    #     context = self.get_context(request, *args, **kwargs)
    #     return render(request, "home/subscribe_page.html", context)

    # Deletes the homepage cache file before updating database
    def save(self, *args, **kwargs):
        cache_ids = ["homepage"]
        for id in cache_ids:
            key = make_template_fragment_key(id)
            cache.delete(key)
        return super().save(*args, **kwargs)