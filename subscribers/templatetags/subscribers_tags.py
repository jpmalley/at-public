from django import template

from ..forms import SubscriberFooterSignUpForm, SubscriberSignUpForm

register = template.Library()

@register.inclusion_tag("subscribers/subscriber_footer_form.html")
def subscriber_footer_form():
    return {"footer_form": SubscriberFooterSignUpForm()}

@register.inclusion_tag("subscribers/subscriber_form.html")
def subscriber_form():
    return {"subscriber_form": SubscriberSignUpForm()}

@register.inclusion_tag("subscribers/webinar_signup_form.html")
def webinar_form():
    return {"subscriber_form": SubscriberSignUpForm()}