from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('api/', include('authentication.urls')),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/', include('contract.urls')),
    path('api/', include('landing.urls')),
    path('api/', include('message.urls')),
    path('api/', include('reminders.urls')),
    path('api/', include('signature.urls')),
    path('api/', include('subscription.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
