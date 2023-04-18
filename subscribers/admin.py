from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Subscriber

class SubscriberAdmin(ModelAdmin):
    """Subscriber admin."""

    model = Subscriber
    menu_label = "Subscribers"
    menu_icon = "group"
    menu_order = 300
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("email", "first", "last",)
    search_fields = ("email", "first", "last",)

modeladmin_register(SubscriberAdmin)