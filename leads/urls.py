from django.urls import path

from leads.views import (
    lead_create,
    lead_delete,
    lead_detail,
    LeadListView,
    lead_update
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('create/', lead_create, name="lead-create"),
    path('delete/<pk>/', lead_delete, name="lead-delete"),
    path('update/<pk>/', lead_update, name="lead-update"),
    path('<pk>/', lead_detail, name="lead-detail"),
]
