from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from leads.models import Lead, User


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent'
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )
        field_classes = {'username': UsernameField}
