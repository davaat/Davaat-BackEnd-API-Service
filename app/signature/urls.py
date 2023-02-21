from django.urls import path
from signature import views

urlpatterns = [
    path('signature_lists', views.SignatureLists.as_view(), name='signature_lists'),
    path('add_signature', views.AddSignature.as_view(), name='add_signature'),
]


