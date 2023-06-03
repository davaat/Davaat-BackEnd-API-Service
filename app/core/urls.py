from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('api/v1/user/', include('authentication.urls')),
    path('api/v1/user/rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/contract/', include('contract.urls')),
    path('api/v1/landing/', include('landing.urls')),
    path('api/v1/message/', include('message.urls')),
    path('api/v1/reminder/', include('reminders.urls')),
    path('api/v1/signature/', include('signature.urls')),
    path('api/v1/subscription/', include('subscription.urls')),
    path('api/v1/tag/', include('tag.urls')),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
