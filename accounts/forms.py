from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# todo default is_active = False
class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and User.objects.filter(email=email).exists():
            raise ValidationError('Email already registered.')
        return email

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email'
        ]
