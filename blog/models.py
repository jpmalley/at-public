"""Flexible page."""
from unicodedata import category, name
from django.db import models
from django import forms
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.shortcuts import render
from django_extensions.db.fields import AutoSlugField
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.snippets.models import register_snippet
from streams import blocks

@register_snippet
class BlogCategory(models.Model):
    """Blog category for a snippet."""

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True, unique=True)

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="New Category")
    ]

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ["title"]

    def __str__(self):
        return self.title


class CategoryMenuItem(Orderable):
    
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="title", editable=True, unique=True)

    page = ParentalKey("blog.BlogHomePage", related_name="menu_items")

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
        ], heading="Menu Item")
    ]

    # def save(self, *args, **kwargs):
    #     cache_ids = ["navigation", "footer_top"]
    #     for id in cache_ids:
    #         key = make_template_fragment_key(id)
    #         cache.delete(key)
    #     return super().save(*args, **kwargs)

class BlogHomePage(RoutablePageMixin, Page):
    """List all Blog Detail Pages."""

    template = "blog/blog_home_page.html"
    
    custom_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Page display title. Overwrites the default title.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        MultiFieldPanel([
            InlinePanel("menu_items", max_num=18, min_num=1, label="Category Menu"),
        ], heading="Category Menu", classname="collapsible"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context"""
        context =  super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public().order_by("-first_published_at")
        context["categories"] = BlogCategory.objects.all()
        return context

    @route(r"^category/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def category_view(self, request, cat_slug):
        """Find blog posts based on a category."""
        context = self.get_context(request)

        try:
            category = BlogCategory.objects.get(slug=cat_slug)
        except Exception:
            category = None

        if category is None:
            pass
        
        context["category"] = category
        context["posts"] = BlogDetailPage.objects.filter(categories__in=[category])
        return render(request, "blog/blog_category_page.html", context)

class BlogDetailPage(Page):
    """Blog detail page."""

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text="Overwrites the default title",
    )

    main_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    main_image_caption = models.CharField(
        max_length=256,
        blank=True,
        null=True,
    )

    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("image_block_extra", blocks.ImageBlockExtra()),
            ("gif_embed_block", blocks.GIFEmbedBlock()),
        ],
        null=True,
        blank=True
    )

    categories = ParentalManyToManyField("blog.BlogCategory", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel('owner'),
        ImageChooserPanel("main_image"),
        FieldPanel("main_image_caption"),
        StreamFieldPanel("content"),
        MultiFieldPanel([
            FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
        ], heading="Categories"),
    ]

    def save(self, *args, **kwargs):
        key = make_template_fragment_key("blog_post_preview", [self.id])
        cache.delete(key)
        return super().save(*args, **kwargs)