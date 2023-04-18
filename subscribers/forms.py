from django import forms

from subscribers.models import Subscriber

class SubscriberFooterSignUpForm(forms.ModelForm):
    """Form to add a new subscriber from the footer."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text

    class Meta:
        model = Subscriber
        fields = ["email", "first"]

class SubscriberSignUpForm(forms.ModelForm):
    """Form to add a new subscriber with all fields."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, value in self.fields.items():
            value.widget.attrs['placeholder'] = value.help_text

    class Meta:
        model = Subscriber
        fields = ["email", "first", "last"]