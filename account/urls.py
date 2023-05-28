
from django.urls import path
from . import views


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

    #dashboard
     path('dashboard', views.dashboard, name='dashboard'),

]