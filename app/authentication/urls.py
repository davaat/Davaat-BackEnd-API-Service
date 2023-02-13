from django.urls import path
from authentication import views

urlpatterns = [
    path('login', views.Login.as_view(), name='Login'),
    path('register', views.Register.as_view(), name='register'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('profile', views.Profile.as_view(), name='profile'),
    path('otp_activation', views.OTPActivation.as_view(), name='otp_activation'),
    path('otp_confirmation', views.OTPConfirmation.as_view(), name='verify'),
    #path('email_activation', views.EmailActivation.as_view(), name='email_activation'),
    #path('otp_confirmation', views.OTPConfirmation.as_view(), name='otp_confirmation'),
    #path('email_confirmation', views.EmailConfirmation.as_view(), name='email_confirmation'),
]


