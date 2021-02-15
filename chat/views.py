from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
from django.views.generic import CreateView

from chat.forms import AuthUserForm, RegisterUserForm


def index(request):
    return render(request, 'chat/index.html')

class MyProjectLoginView(LoginView):
    template_name = 'chat/login.html'
    form_class = AuthUserForm
    success_url = '/'
    def get_success_url(self):
        return self.success_url

class RegisterUserView(CreateView):
    model = User
    template_name = 'chat/register.html'
    form_class = RegisterUserForm
    success_url = '/'
    success_msg = 'Пользователь успешно создан'

class MyProjectLogout(LogoutView):
    next_page = '/'