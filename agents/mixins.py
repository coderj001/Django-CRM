from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class OrganisorLoginRequiredMixin(LoginRequiredMixin):
    """Verify that the current user is authenticated is organisor."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organisor:
            return redirect(reverse_lazy('landing-page'))
        return super().dispatch(request, *args, **kwargs)
