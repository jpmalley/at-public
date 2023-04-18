from django import forms
from django.contrib.auth.models import Group

from users.models import User
from allauth.account.forms import SignupForm

class UserUpdateNameForm(forms.ModelForm):
    """Form to add name to user."""
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class WorkshopSignUpForm(forms.Form):
    """Form to create account after payment"""
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    email = forms.EmailField(label='Email address', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    transaction_id = forms.CharField(label='Transaction ID', max_length=100, widget=forms.HiddenInput)