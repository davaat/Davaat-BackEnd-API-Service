from django.urls import path, include
from authentication import views


urlpatterns = [
    path('company_login', views.CompanyLogin.as_view(), name='company_login'),
    path('company_register', views.CompanyRegister.as_view(), name='company_register'),
    path('user_register', views.UserRegister.as_view(), name='user_register'),
    path('user_login', views.UserLogin.as_view(), name='user_login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('profile', views.Profile.as_view(), name='profile'),
    path('otp_confirmation', views.OTPConfirmation.as_view(), name='verify'),
    #path('email_activation', views.EmailActivation.as_view(), name='email_activation'),
    #path('otp_confirmation', views.OTPConfirmation.as_view(), name='otp_confirmation'),
    #path('email_confirmation', views.EmailConfirmation.as_view(), name='email_confirmation'),
    path('reset_pass', views.ResetPass.as_view(), name='ResetPass'),
    path('reset_pass_conf', views.ResetPassConf.as_view(), name='ResetPassConf'),
]
