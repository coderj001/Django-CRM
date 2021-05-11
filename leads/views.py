from django.shortcuts import render
from leads.forms import LeadForm

from leads.models import Lead


def landing_page(request):
    return render(request, "utils/landing.html")


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context=context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context=context)


def lead_create(request):
    context = {"form": LeadForm()}
    return render(request, "leads/lead_create.html", context=context)
