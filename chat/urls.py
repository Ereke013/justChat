from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'chat_home'),
    path('login', views.MyProjectLoginView.as_view(), name='login-page')
]
