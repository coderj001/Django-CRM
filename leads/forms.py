from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from leads.models import Lead, User, Agent


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'agent',
            'category'
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", )
        field_classes = {'username': UsernameField}


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = agents
