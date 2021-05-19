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

from leads.forms import LeadForm, CustomUserCreationForm
from leads.models import Lead
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")


class LandingPageView(TemplateView):
    template_name = "utils/landing.html"


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"
    login_url = reverse_lazy('login')


class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"
    login_url = reverse_lazy('login')


class LeadCreateView(LoginRequiredMixin, CreateView):
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
    queryset = Lead.objects.all()
    form_class = LeadForm
    success_url = reverse_lazy("leads:lead-list")
    login_url = reverse_lazy('login')


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()
    success_url = reverse_lazy("leads:lead-list")
    login_url = reverse_lazy('login')
