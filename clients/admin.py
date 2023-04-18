from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import Client

class ClientAdmin(ModelAdmin):
    """Client admin."""

    model = Client
    menu_label = "Clients"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("email", "first", "last",)
    search_fields = ("email", "first", "last",)

modeladmin_register(ClientAdmin)