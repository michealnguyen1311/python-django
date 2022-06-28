import django
from django.forms.models import ModelForm
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http.response import HttpResponse
from django.db.models import Q 
import time
import datetime
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.conf import settings
from .forms import RegistrationForm, LoginForm

def register_user(request):
    register_form = RegistrationForm()
    if request.method =="POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save_user()
            
    return render(
        request=request,
        template_name='user/register.html',
        context={
            'register_form': register_form
        }
    )
def login_user(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(
                username=login_form.cleaned_data['username'],
                password=login_form.cleaned_data['password']
            )
            if user:
                login(request, user)
                if request.GET.get('next', None):
                    return HttpResponseRedirect(request.GET.get('next'))
                return redirect('index')
            else:
                print("Thông tin đăng nhập không đúng. Vui lòng kiểm tra lại")
    return render(
            request=request,
            template_name='user/login.html',
            context={
            'login_form': login_form
            }
        )