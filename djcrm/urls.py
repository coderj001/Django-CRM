from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
    PasswordResetCompleteView
)
from django.urls import include, path

from leads.views import LandingPageView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name="landing-page"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('reset-password/', PasswordResetView.as_view(), name="password-reset"),
    path('password-reset-done/', PasswordResetDoneView.as_view(),
         name="password_reset_done"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(),
         name="password_reset_complete"),
    path('password-reset-confirm/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('leads/', include('leads.urls')),
    path('agents/', include('agents.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
