from django.urls import path
from contract import views

urlpatterns = [
    path('contract_lists', views.ContractLists.as_view(), name='contract_lists'),
    path('add_contract', views.AddContract.as_view(), name='add_contract'),
    path('upload_contract', views.UploadContract.as_view(), name='upload_contract'),
    path('user_questionnaire_list', views.UserQuestionnaireList.as_view(), name='user_questionnaire_list'),
    path('add_questionnaire', views.AddQuestionnaire.as_view(), name='add_questionnaire'),
    path('cat_list', views.Catlist.as_view(), name='cat_list'),
    path('add_cat', views.AddCat.as_view(), name='add_cat'),
    path('contract_library', views.Contractlibrary.as_view(), name='contract_library'),
    path('add_contract_library', views.AddContractLibrary.as_view(), name='add_contract_library'),
]


