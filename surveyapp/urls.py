from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('submit-survey', views.submit_survey, name= "submit_survey"),
    path('login', views.login, name= "login"),
    path('logout', views.logout, name= "logout"),
    path('result', views.result, name= "result")
]