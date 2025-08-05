from django.urls import path
from .views import SurvivorSignUp,SurvivorLogIn

urlpatterns = [
    path('signup/',SurvivorSignUp.as_view(),name='signup'),
    path('login/',SurvivorLogIn.as_view(),name='login'),
]