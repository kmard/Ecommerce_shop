
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('register',views.register,name='register'),

    #email verification URL's

    path('email-verifiacation/<str:uidb64>/<str:token>/',views.email_verification,name='email-verifiacation'),

    path('email-verifiacation-sent',views.email_verification_sent,name='email-verifiacation-sent'),

    path('email-verifiacation-success', views.email_verification_success, name='email-verifiacation-success'),

    path('email-verifiacation-failed', views.email_verification_failed, name='email-verifiacation-failed'),

    #login /logout url
    path('my-login', views.my_login, name='my-login'),

    path('user-logout', views.user_logout, name='user-logout'),

    #dashboard / profile urls
     path('dashboard', views.dashboard, name='dashboard'),

     path('profile-management', views.profile_management, name='profile-management'),

     path('delete-account', views.delete_account, name='delete-account'),

    #password management urls/views

    #1) Submit our email form
    path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),

    #2)Success message stating that a password reset email was sent
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    #3) Password reset link
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    #4)Success message starting that our password was reset
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),





]