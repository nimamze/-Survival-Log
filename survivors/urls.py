from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.SurvivorSignUp.as_view(),name='signUp'),
    path('login/',views.SurvivorLogIn.as_view(),name='login'),
    path('loglist/',views.SurvivorLog.as_view(),name = 'loglist'),
    path('createlog/',views.createloge.as_view()),
    path('loglist/<int:pk>/',views.createLog.as_view(),name = 'loglit'),
    path('logout/',views.LogoutView.as_view())

]