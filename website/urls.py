from django.urls import path
from . import views


urlpatterns = [
    path('information/setup/', views.SetUpInformation),
]
