from django.urls import path
from contract import views

urlpatterns = [
    path('contract_lists', views.ContractLists.as_view(), name='contract_lists'),
    path('add_contract', views.AddContract.as_view(), name='add_contract'),
]


