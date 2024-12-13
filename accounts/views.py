from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from accounts.forms import CreateUserForm


def register_view(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.instance.is_active = False
            form.save()
            return redirect(reverse_lazy('e_verify'))
    return render(request, 'auth/sign-up.html', context={'form': form})


def login_view(request):
    return render(request, 'auth/sign-in.html')


def email_verification_view(request):
    return render(request, 'auth/email_verification.html')
