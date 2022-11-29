from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('firstName', 'secondName', 'phoneNumber', 'address')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = ('firstName', 'secondName', 'phoneNumber', 'address')