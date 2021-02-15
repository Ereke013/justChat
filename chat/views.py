from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
from chat.forms import AuthUserForm


def index(request):
    return render(request, 'chat/index.html')

class MyProjectLoginView(LoginView):
    template_name = 'chat/login.html'
    form_class = AuthUserForm
    success_url = '/'

# class RegisterUserView()