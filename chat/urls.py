from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'chat_home'),
    path('login', views.MyProjectLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.MyProjectLogout.as_view(), name='logout'),
    path('sendmsg/<int:pk>/<int:id>', views.MessageSendView, name='msg_send')
]
