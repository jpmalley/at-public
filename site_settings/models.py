from django.db import models
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMedia(BaseSetting):
    """Global social media settings."""

    # facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    # twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    instagram = models.URLField(blank=True, null=True, help_text="Intagram URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel")
    linkedin = models.URLField(blank=True, null=True, help_text="LinkedIn URL")
    medium = models.URLField(blank=True, null=True, help_text="Medium URL")
    spotify = models.URLField(blank=True, null=True, help_text="Spotify URL")

    panels = [
        MultiFieldPanel([
            # FieldPanel("facebook"),
            # FieldPanel("twitter"),
            FieldPanel("instagram"),
            FieldPanel("youtube"),
            FieldPanel("linkedin"),
            FieldPanel("medium"),
            FieldPanel("spotify"),
        ], heading="Social Media Settings")
    ]

    def save(self, *args, **kwargs):
        cache_ids = ["footer_bottom"]
        for id in cache_ids:
            key = make_template_fragment_key(id)
            cache.delete(key)
        return super().save(*args, **kwargs)