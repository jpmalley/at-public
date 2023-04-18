from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

from flex import views as flex_views
from users import views as users_views
from paypal import views as paypal_views

urlpatterns = [
    path('django-admin/', admin.site.urls),

    path('admin/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),

    path(r'account/', include('allauth.urls')),
    path('account/', users_views.account, name='account_home'),
    path('account/name/', users_views.user_update_name_form),
    path('account/thank-you-set-password/', users_views.thank_you_set_password, name='thank_you_set_password'),

    path('payments/capture-paypal-transaction/', paypal_views.capture_paypal_transaction),

    path('search/', search_views.search, name='search'),

    path("page/biz-vip-confirmation/", flex_views.biz_vip_confirmation),
    path("consultation-confirmation/", flex_views.consultation_confirmation),
    path("scaleyourbiz/", flex_views.scale_your_biz_landing),
    path("advocate-workshop-old/", flex_views.advocate_workshop, name='advocate'),
    # path("self-advocate-audaciously/", flex_views.self_advocate_audaciously, name='self_advocate_audaciously'),
    # path("self-advocate-audaciously/congrats-youre-in/", flex_views.congrats_your_in, name='congrats_youre_in'),
    path("hsr/congrats-youre-in/", flex_views.congrats_your_in, name='congrats_youre_in'),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
