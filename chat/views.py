import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
# Create your views here.
from django.views.generic import CreateView
from django.http import JsonResponse, HttpResponse
from chat.forms import AuthUserForm, RegisterUserForm


def index(request):
    messages = Message.objects.all()
    # message_title=Group.objects.all()
    message_title=Group.objects.get(id=1)
    return render(request, 'chat/index.html', {'messages': messages, 'message_title':message_title})

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

def MessageSendView(request, pk, id):
    print("keldi 667 ")
    user = User.objects.get(id=id)
    group = Group.objects.get(id=pk)
    if request.is_ajax() and request.POST:

        message = Message.objects.create(message_text=request.POST.get('message_text'), date=datetime.datetime.now(), user=user, group=group)
        # return JsonResponse({}, safe=True, status=200)


    message = list(Message.objects.filter( group=group).order_by("date").values('date', 'user__first_name', 'user__last_name', 'message_text', "user"))
    user_id = []
    user_id.append(request.user.id)
    return JsonResponse({'message': message, 'user_id':user_id}, safe=True, status=200)