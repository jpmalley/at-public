from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django import forms

from users.models import User
from users.forms import UserUpdateNameForm, WorkshopSignUpForm
from paypal.models import PayPalTransaction

# Create your views here.
@login_required
def account(request):
    context = {}
    return render(request, 'users/account.html', context)

@login_required
def user_update_name_form(request, *args, **kwargs):
    user_id = request.user.id
    current_user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        form = UserUpdateNameForm(request.POST)
        if form.is_valid():
            updated_user = form.save(commit=False)
            current_user.first_name = updated_user.first_name
            current_user.last_name = updated_user.last_name
            current_user.save()
            context = {
                'form': form,
            }
            return render(request, 'users/user_update_name.html', context)
    else:
        form = UserUpdateNameForm(initial=model_to_dict(current_user))

    context = {
        'form': form,
    }
    return render(request, "users/user_update_name.html", context)


def thank_you_set_password(request, *args, **kwargs):
    context = {}
    status = request.GET.get('status', 'None')
    transaction_id = request.GET.get('transaction_id','None')
    print(transaction_id)
    
    if status == 'COMPLETED':
        transaction = get_object_or_404(PayPalTransaction, transaction_id=transaction_id)
        if transaction:
            if transaction.associated == False:
                first_name = transaction.buyer_first_name
                last_name = transaction.buyer_last_name
                email = transaction.buyer_email
                form = WorkshopSignUpForm(initial={
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'transaction_id': transaction_id,
                })
                context = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'form':form,
                    }
            else:
                error_message = "Your transactions has already been associated with an account. If you believe this to be an error, please contact us."
                cta_message = "Contact Us"
                cta_link = "mailto:hello@alexandriathibodeaux.com"
                context = {
                    'error_message': error_message,
                    'cta_message': cta_message,
                    'cta_link': cta_link,
                    }
                return render(request, 'users/oops_something_went_wrong.html', context)
        else:
            error_message = "We could not confirm your transaction."
            cta_message = "Contact Us"
            cta_link = "mailto:hello@alexandriathibodeaux.com"
            context = {
                'error_message': error_message,
                'cta_message': cta_message,
                'cta_link': cta_link,
                }
            return render(request, 'users/oops_something_went_wrong.html', context)

    if request.method == "POST":
        form = WorkshopSignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            transaction_id = form.cleaned_data['transaction_id']

            if not User.objects.filter(email=email).exists():
                new_user = User.objects.create_user(email=email, password=password)
                new_user.first_name = first_name
                new_user.last_name = last_name
                clients_paid = Group.objects.get(name='Clients - Paid')
                clients_paid.user_set.add(new_user)
                new_user.save()
                transaction = get_object_or_404(PayPalTransaction, transaction_id=transaction_id)
                transaction.associated = True
                transaction.save()
                auth_user = authenticate(request, username=email, password=password)
                login(request, auth_user)
                return redirect(reverse('account_home'))
            else:
                error_message = "A user already exists with this email."
                cta_message = "Try another"
                cta_link = "javascript:history.back()"
                context = {
                    'error_message': error_message,
                    'cta_message': cta_message,
                    'cta_link': cta_link,
                    }
                return render(request, 'users/oops_something_went_wrong.html', context) 
    
    return render(request, 'users/thank_you_set_password.html', context)