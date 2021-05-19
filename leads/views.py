from django.shortcuts import redirect, render
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


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")


class LandingPageView(TemplateView):
    template_name = "utils/landing.html"


class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(DetailView):
    model = Lead
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"


class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadForm
    success_url = reverse_lazy("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject="A lead has been created",
            message="Go to the site to see new lead",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super(LeadCreateView, self).form_valid(form)


class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadForm
    success_url = reverse_lazy("leads:lead-list")


class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    success_url = reverse_lazy("leads:lead-list")
