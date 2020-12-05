from django.contrib.auth.decorators import login_required
from django.views.generic import View, CreateView
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings

from core import forms
from core import models


@login_required(login_url='login')
def index(request):
    data = models.Teacher.objects.get(email=request.user)

    return render(request, 'index.html', {'data': data})


def loginUser(request):
    form = forms.LoginForm(request.POST or None)

    context = {
        "form": form
    }
    if form.is_valid():
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        if user is None:
            # messages.info(request, "Mail və ya şifrə yanlışdır")
            return render(request, 'login.html', context)

        # messages.success(request, "Uğurla giriş etdiniz")
        login(request, user)
        return redirect('index')
    return render(request, 'login.html', context)


def registerUser(request):
    form = forms.RegisterUserForm(request.POST or None)
    if form.is_valid():

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        name = form.cleaned_data.get("name")

        newUser = models.Teacher(email=email, name=name)
        newUser.set_password(password)

        newUser.save()
        login(request, newUser)
        return redirect('index')
    context = {
        "form": form
    }
    return render(request, 'register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')


def groupsView(request):
    data = models.Teacher.objects.get(
        email=request.user)

    #subjects = [subject for subject in models.Teacher.objects.get(email=request.user).subjects.all() if subject in groups.subjects.all()]
    return render(request, 'groups.html', {'data': data})
