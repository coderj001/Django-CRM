from django.urls import path

from leads.views import lead_create, lead_detail, lead_list

app_name = "leads"

urlpatterns = [
    path('', lead_list, name="lead-list"),
    path('create/', lead_create, name="lead-create"),
    path('<pk>/', lead_detail, name="lead-detail"),
]
