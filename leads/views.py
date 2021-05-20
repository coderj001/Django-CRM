from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView
)

from agents.mixins import LoginRequiredMixin, OrganisorLoginRequiredMixin
from leads.forms import CustomUserCreationForm, LeadForm
from leads.models import Lead


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")


class LandingPageView(TemplateView):
    template_name = "utils/landing.html"


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"
    login_url = reverse_lazy('login')

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"
    login_url = reverse_lazy('login')

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadCreateView(OrganisorLoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadForm
    success_url = reverse_lazy("leads:lead-list")
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadForm
    success_url = reverse_lazy("leads:lead-list")
    login_url = reverse_lazy('login')

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    success_url = reverse_lazy("leads:lead-list")
    login_url = reverse_lazy('login')

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset
