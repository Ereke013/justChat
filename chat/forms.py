from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, PasswordInput
from django.shortcuts import redirect

from .models import *

class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password')

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'username...'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'password...'
            })
        }

    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('username', 'password', 'first_name', 'last_name')

        widgets={
            "username":TextInput(attrs={
                'class':'form-control',
                'placeholder': 'username...'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'password...'
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'first_name...'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'last_name...'
            })
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            person = Person.objects.create(user=user, group_id=1)
            person.save()
