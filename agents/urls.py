from django.urls import path
from agents.views import (
    AgentListView,
    AgentCreateView,
    AgentDetailView,
    AgentUpdateView,
    AgentDeleteView
)


app_name = "agents"

urlpatterns = [
    path('', AgentListView.as_view(), name="agent-list"),
    path('create/', AgentCreateView.as_view(), name="agent-create"),
    path('update/<pk>/', AgentUpdateView.as_view(), name="agent-update"),
    path('delete/<pk>/', AgentDeleteView.as_view(), name="agent-delete"),
    path('<pk>/', AgentDetailView.as_view(), name="agent-detail"),
]
