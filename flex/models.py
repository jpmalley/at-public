"""Flexible page."""
from django.db import models
from django.shortcuts import render
from django.conf import settings

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from streams import blocks

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

class FlexPage(Page):
    """Flexible page class."""

    template = "flex/flex_page.html"

    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"
    IMAGE_POSITION_CHOICES = [
        (TOP, "Top"),
        (CENTER, "Center"),
        (BOTTOM, "Bottom"),
    ]

    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("image", blocks.ImageBlock()),
            ("button", blocks.ButtonBlock()),
            ("headline", blocks.HeadlineBlock()),
            ("left_image", blocks.LeftImageBlock()),
            ("image_row", blocks.ImageRowBlock()),
            ("image_carousel", blocks.ImageCarouselBlock()),
        ],
        null=True,
        blank=True
    )

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

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        MultiFieldPanel([
            ImageChooserPanel("header_image"),
            FieldPanel("header_image_position"),
        ], heading="Header Image", classname="collapsible"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"

class PressLink(Orderable):
    """Press link orderable"""

    link_text = models.CharField(max_length=100)
    link_desc = models.CharField(max_length=100, null=True, blank=True)
    link_url = models.URLField()
    page = ParentalKey(
        "flex.PressPageSection", 
        related_name="press_link",
        on_delete=models.CASCADE,
    )

    panels = [
        FieldPanel("link_text"),
        FieldPanel("link_desc"),
        FieldPanel("link_url"),
    ]

class PressPageSection(ClusterableModel):
    """Page section orderable"""

    section_title = models.CharField(max_length=100, null=False, blank=True)
    page = ParentalKey(
        "flex.PressPage", 
        related_name="press_sections",
        on_delete=models.CASCADE,
    )

    panels = [
        FieldPanel("section_title"),
        InlinePanel("press_link", label="Press Link"),
    ]

class PressPage(Page):
    """Press page class"""

    template = "flex/press_page.html"

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

    top_content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("image", blocks.ImageBlock()),
            ("button", blocks.ButtonBlock()),
            ("headline", blocks.HeadlineBlock()),
            ("left_image", blocks.LeftImageBlock()),
            ("image_row", blocks.ImageRowBlock()),
            ("image_carousel", blocks.ImageCarouselBlock()),
        ],
        null=True,
        blank=True
    )

    carousel_content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("headline", blocks.HeadlineBlock()),
            ("image_carousel", blocks.ImageCarouselBlock()),
        ],
        null=True,
        blank=True
    )

    bottom_content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("image", blocks.ImageBlock()),
            ("button", blocks.ButtonBlock()),
            ("headline", blocks.HeadlineBlock()),
            ("left_image", blocks.LeftImageBlock()),
            ("image_row", blocks.ImageRowBlock()),
            ("image_carousel", blocks.ImageCarouselBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        MultiFieldPanel([
            ImageChooserPanel("header_image"),
            FieldPanel("header_image_position"),
        ], heading="Header Image", classname="collapsible"),
        StreamFieldPanel("top_content"),
        MultiFieldPanel([
            InlinePanel("press_sections", label="Section")
        ], heading="Sections"),
        StreamFieldPanel("carousel_content"),
        StreamFieldPanel("bottom_content"),
    ]

class LandingPage(Page):
    """Landing page class."""

    template = "flex/landing_page.html"

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

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("header_image")
    ]
    class Meta:
        verbose_name = "Landing Page"
        verbose_name_plural = "Landing Pages"

class LandingPageBiz(LandingPage):
    """Landing page class."""

    template = "flex/landing_page_biz.html"
    class Meta:
        verbose_name = "Landing Page (biz)"
        verbose_name_plural = "Landing Pages (biz)"

class ExclusiveContentPage(Page):
    """Exclusive page class."""

    template = "flex/exclusive_content_page.html"

    custom_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Page display title. Overwrites the default title.",
    )

    video_embed_code = models.TextField(
        blank=True,
        null=True,
        help_text="Paste Wistia embed code here."
    )

    content = StreamField(
        [
            ("full_richtext", blocks.RichTextBlock()),
            ("image", blocks.ImageBlock()),
            ("button", blocks.ButtonBlock()),
            ("headline", blocks.HeadlineBlock()),
            ("left_image", blocks.LeftImageBlock()),
            ("image_row", blocks.ImageRowBlock()),
            ("image_carousel", blocks.ImageCarouselBlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("video_embed_code"),
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Exclusive Page"
        verbose_name_plural = "Exclusive Pages"

    
class WebinarPage(Page):
    """Webinar page class."""

    template = "flex/webinar_page.html"

    custom_title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        default="How to Advocate for Yourself by Setting Boundaries",
    )

    webinar_date = models.DateTimeField(
        null=True,
        blank=False,
    )

    mailchimp_tags = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    mailchimp_list_id = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        default="314c20dfea",
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("webinar_date"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel("mailchimp_tags", classname="col6"),
                FieldPanel("mailchimp_list_id", classname="col6")
            ]),
        ], heading="Mailchimp Settings"),
    ]

    class Meta:
        verbose_name = "Webinar Page"
        verbose_name_plural = "Webinar Pages"

    def serve(self, request, *args, **kwargs):
        from subscribers.forms import SubscriberSignUpForm
        context = self.get_context(request, *args, **kwargs)
        if request.method == "POST":
            form = SubscriberSignUpForm(request.POST)
            context["form"] = form
            if form.is_valid():
                subscriber = form.save()

                mailchimp = MailchimpMarketing.Client()
                mailchimp.set_config({
                    "api_key": "af052db97d0a02f90ebe1db205bf559d-us20",
                    "server": "us20"
                })

                list_id = self.mailchimp_list_id
                subscriber_tags = [self.mailchimp_tags]
                
                member_info = {
                    "email_address": subscriber.email,
                    "status": "subscribed",
                    "merge_fields": {
                        "FNAME": subscriber.first,
                        "LNAME": subscriber.last
                    },
                    "tags": subscriber_tags
                }

                try:
                    response = mailchimp.lists.add_list_member(list_id, member_info)
                    # print("response: {}".format(response))
                except ApiClientError as error:
                    print("An exception occurred: {}".format(error.text))

                context["subscriber"] = subscriber

                response = render(request, "flex/webinar_confirmation.html", context)

                return response
        else:
            form = SubscriberSignUpForm()

        context["form"] = form

        return render(request, "flex/webinar_page.html", context)


class ProgramPage(Page):
    """Program page class."""

    template = "flex/program_page.html"

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default="Self-Advocate Audaciously",
    )

    program_price = models.DecimalField(
        max_digits=7, 
        decimal_places=2,
        blank=False,
        null=True,
        default=1000.00,
    )

    paypal_client_id = settings.PAYPAL_CLIENT_ID

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("program_price"),
    ]

    class Meta:
        verbose_name = "Program Page"
        verbose_name_plural = "Program Pages"

class HighlySensitiveRadical(Page):
    """Program page class."""

    template = "pages/highly-sensitive-radical.html"

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        default="Becoming a Highly Sensitive Radical",
    )

    program_price = models.DecimalField(
        max_digits=7, 
        decimal_places=2,
        blank=False,
        null=True,
        default=129.00,
    )

    paypal_client_id = settings.PAYPAL_CLIENT_ID

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("program_price"),
    ]

    class Meta:
        verbose_name = "HSR Page"
        verbose_name_plural = "HSR Pages"