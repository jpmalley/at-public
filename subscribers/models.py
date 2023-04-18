from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField
from streams import blocks

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

class Subscriber(models.Model):
    """A subscriber model"""

    email = models.CharField(
        max_length=100, 
        blank=False, 
        null=False, 
        help_text='Email address',
    )
    first = models.CharField(
        max_length=100, 
        blank=False, 
        null=False, 
        help_text='First name',
    )
    last = models.CharField(
        max_length=100, 
        blank=True, 
        null=False, 
        help_text='Last name',
    )
    source = models.CharField(
        max_length=100, 
        blank=True, 
        null=False, 
        help_text='Sign up origin',
    )

    def __str__(self):
        return self.first + self.last

    class Meta: #no_qa
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"


class SubscribePage(Page):

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

    thank_you_text = StreamField(
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

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        MultiFieldPanel([
            ImageChooserPanel("header_image"),
            FieldPanel("header_image_position"),
        ], heading="Header Image", classname="collapsible"),
        StreamFieldPanel("content"),
        StreamFieldPanel("thank_you_text"),
    ]

    def serve(self, request, *args, **kwargs):
        from .forms import SubscriberSignUpForm

        if request.method == "POST":
            form = SubscriberSignUpForm(request.POST)
            if form.is_valid():
                subscriber = form.save()

                mailchimp = MailchimpMarketing.Client()
                mailchimp.set_config({
                    "api_key": "af052db97d0a02f90ebe1db205bf559d-us20",
                    "server": "us20"
                })

                list_id = "b9f57a70b5"
                
                member_info = {
                    "email_address": subscriber.email,
                    "status": "subscribed",
                    "merge_fields": {
                        "FNAME": subscriber.first,
                        "LNAME": subscriber.last
                    }
                }

                try:
                    response = mailchimp.lists.add_list_member(list_id, member_info)
                    # print("response: {}".format(response))
                except ApiClientError as error:
                    print("An exception occurred: {}".format(error.text))

                context = self.get_context(request, *args, **kwargs)
                context["subscriber"] = subscriber

                response = render(request, "subscribers/thank_you.html", context)
                response.set_cookie("subscribed_email", "True")

                return response
        else:
            form = SubscriberSignUpForm()

        context = self.get_context(request, *args, **kwargs)
        context["form"] = form

        return render(request, "subscribers/subscribe_page.html", context)