from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from agents.forms import AgentModelForm
from leads.models import Agent


class AgentListView(LoginRequiredMixin, ListView):
    template_name = "agents/agent_list.html"

    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Agent.objects.all()


class AgentCreateView(LoginRequiredMixin, CreateView):
    template_name = "agents/agent_create.html"
    form_class = AgentModelForm
    success_url = reverse_lazy("agents:agent-list")
    context_object_name = "agents"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.organisation = self.request.user.userprofile
        instance.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(LoginRequiredMixin, DetailView):
    model = Agent
    template_name = "agents/agent_detail.html"
    context_object_name = "agent"
    login_url = reverse_lazy('login')
