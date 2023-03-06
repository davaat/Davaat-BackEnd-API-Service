from django.urls import path
from signature import views

urlpatterns = [
    path('', views.SignatureLists.as_view(), name='signature_lists'),
    path('', views.AddSignature.as_view(), name='add_signature'),
]


