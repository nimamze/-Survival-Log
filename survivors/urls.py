from django.urls import path
from . import views

urlpatterns = [
    path('signUp/',views.SurvivorSignUp.as_view(),name='signUp'),
    path('logIn/',views.SurvivorLogIn.as_view(),name='login'),
]