from core import forms
from core import models
from django.contrib.auth.decorators import login_required
from django.views.generic import View, CreateView
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings


@login_required(login_url='login')
def index(request):
    data = models.Teacher.objects.get(email=request.user)
    print(request.user)
    return render(request, 'index.html', {'data': data})


def loginUser(request):
    form = forms.LoginForm(request.POST or None)

    context = {
        "form": form
    }
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('index')
    return render(request, 'index.html', context)


def registerUser(request):
    form = forms.RegisterUserForm(request.POST or None)
    if form.is_valid():

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        newUser = models.Teacher(email=email)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        return redirect('index')
    context = {
        "form": form
    }
    return render(request, 'register.html', context)
