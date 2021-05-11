import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from leads.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name="landing-page"),
    path('leads/', include('leads.urls')),
]

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
