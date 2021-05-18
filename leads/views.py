from django.shortcuts import redirect, render

from leads.forms import LeadForm
from leads.models import Lead
from django.views.generic import TemplateView, ListView


class LandingPageView(TemplateView):
    template_name = "utils/landing.html"


class LeadListView(ListView):
    template_name = "leads.lead_list.html"
    queryset = Lead.objects.all()


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
    form = None
    if request.method == 'GET':
        form = LeadForm()
    else:
        form = LeadForm(request.POST or None)
        if form.is_valid():
            instant = form.save()
            return redirect('leads:lead-detail', instant.id)
    context = {"form": form}
    return render(request, "leads/lead_create.html", context=context)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = None
    if request.method == 'POST':
        form = LeadForm(request.POST or None)
        if form.is_valid():
            instant = form.save()
            return redirect('leads:lead-detail', instant.id)

    form = LeadForm(instance=lead)
    context = {
        "lead": lead,
        "form": form,
    }
    return render(request, "leads/lead_update.html", context=context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('leads:lead-list')
    context = {"lead": lead}
    return render(request, "leads/lead_delete.html", context=context)
