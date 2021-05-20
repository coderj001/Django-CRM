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
        instance.organisation = self.request.user.userprofile
        instance.save()
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
