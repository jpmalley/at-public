from django.shortcuts import render

from django.conf import settings

import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError

# Create your views here.
def biz_vip_confirmation(request):
    return render(request, "pages/biz_vip_confirmation.html")

def consultation_confirmation(request):
    return render(request, "pages/consultation_confirmation.html")

def scale_your_biz_landing(request):
    context = {
        "paypal_client_id": settings.PAYPAL_CLIENT_ID
    }
    return render(request, "pages/scale_landing_page.html", context)

def advocate_workshop(request):
    from subscribers.forms import SubscriberSignUpForm
    context = {}
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

            list_id = "314c20dfea"
            subscriber_tags = ["Dec 28"]
            
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

            response = render(request, "pages/advocate_confirmation.html", context)

            return response
    else:
        form = SubscriberSignUpForm()

    context["form"] = form
    return render(request, "pages/advocate_lp.html", context)

def self_advocate_audaciously(request):
    context = {
        "paypal_client_id": settings.PAYPAL_CLIENT_ID
    }
    return render(request, "pages/self_advocate_audaciously.html", context)

def congrats_your_in(request):
    return render(request, "pages/congrats_youre_in.html")