
from django.urls import path
from . import views


urlpatterns = [

    path('register',views.register,name='register'),

    #email verification URL's

    path('email-verifiacation',views.email_verification,name='email-verifiacation'),

    path('email-verifiacation-sent',views.email_verification_sent,name='email-verifiacation-sent'),

    path('email-verifiacation-success', views.email_verification_success, name='email-verifiacation-success'),

    path('email-verifiacation-failed', views.email_verification_failed, name='email-verifiacation-failed'),


]