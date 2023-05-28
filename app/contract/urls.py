from django.urls import path
from contract import views

urlpatterns = [
    path('contract_lists', views.ContractLists.as_view(), name='contract_lists'),
    path('add_contract', views.AddContract.as_view(), name='add_contract'),
    path('upload_contract', views.UploadContract.as_view(), name='upload_contract'),
    path('user_questionnaire_list', views.UserQuestionnaireList.as_view(), name='user_questionnaire_list'),
    path('add_questionnaire', views.AddQuestionnaire.as_view(), name='add_questionnaire'),
]


