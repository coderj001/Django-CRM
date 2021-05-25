from django.urls import path

from leads.views import (
    LeadCreateView,
    LeadDeleteView,
    LeadDetailView,
    LeadListView,
    LeadUpdateView,
    AssignAgentView,
    CategoryListView,
    CategoryDetailView
)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),
    path('create/', LeadCreateView.as_view(), name="lead-create"),
    path('categories/', CategoryListView.as_view(), name="category-list"),
    path('categories/<int:pk>/', CategoryDetailView.as_view(),
         name="category-detail"),
    path('delete/<int:pk>/', LeadDeleteView.as_view(), name="lead-delete"),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name="lead-update"),
    path('<int:pk>/assign_agent/', AssignAgentView.as_view(),
         name="lead-assign-agent"),
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-detail"),
]
