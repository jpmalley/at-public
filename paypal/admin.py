from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import PayPalTransaction

class PayPalAdmin(ModelAdmin):
    """PayPal admin."""

    model = PayPalTransaction
    menu_label = "PayPal"
    menu_icon = "group"
    menu_order = 300
    add_to_settings_menu = True
    exclude_from_explorer = False
    list_display = ("transaction_id", "status", "buyer_first_name", "buyer_last_name", "buyer_email", "associated")
    search_fields = ("transaction_id", "status", "buyer_first_name", "buyer_last_name", "buyer_email", "associated")

modeladmin_register(PayPalAdmin)