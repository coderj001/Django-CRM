from random import randint

from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from agents.forms import AgentModelForm
from agents.mixins import OrganisorLoginRequiredMixin
from leads.models import Agent


class AgentListView(OrganisorLoginRequiredMixin, ListView):
    template_name = "agents/agent_list.html"
    context_object_name = "agents"

    login_url = reverse_lazy('login')

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentCreateView(OrganisorLoginRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    success_url = reverse_lazy("agents:agent-list")

    login_url = reverse_lazy('login')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.is_agent = True
        instance.is_organisor = False
        instance.set_password(f"password{randint(100,100000)}")
        instance.save()
        Agent.objects.create(
            user=instance, organisation=self.request.user.userprofile)
        send_mail(
            subject="You are invited to be an agent.",
            message="You are added as agent in DJCRM, please login to continue.",
            from_email="test@test.com",
            recipient_list=[instance.email]
        )
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganisorLoginRequiredMixin, DetailView):
    model = Agent
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"

    login_url = reverse_lazy('login')

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentUpdateView(OrganisorLoginRequiredMixin, UpdateView):
    template_name = "agents/agent_update.html"
    form_class = AgentModelForm
    success_url = reverse_lazy("agents:agent-list")

    login_url = reverse_lazy('login')

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)


class AgentDeleteView(OrganisorLoginRequiredMixin, DeleteView):
    template_name = "agents/agent_delete.html"
    success_url = reverse_lazy("agents:agent-list")

    login_url = reverse_lazy('login')

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
