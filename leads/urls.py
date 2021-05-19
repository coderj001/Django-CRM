from django.urls import path

from leads.views import (
    LeadCreateView,
    LeadDeleteView,
    LeadDetailView,
    LeadListView,
    LeadUpdateView,
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('create/', LeadCreateView.as_view(), name="lead-create"),
    path('delete/<pk>/', LeadDeleteView.as_view(), name="lead-delete"),
    path('update/<pk>/', LeadUpdateView.as_view(), name="lead-update"),
    path('<pk>/', LeadDetailView.as_view(), name="lead-detail"),
]
