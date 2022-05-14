from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])
            if user:
                login(request, user)
                return redirect(reverse("home:index"))
            else:
                return HttpResponse("Wrong username or password, please try again.")
        else:
            return HttpResponse("Invaild username or password.")
    elif request.method == "GET":
        user_login_form = UserLoginForm()
        context = {"form": user_login_form}
        return render(request, "accounts/templates/login.html", context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("home:index"))


def user_register(request):
    if request.method == "POST":
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            new_user = user_register_form.save(commit=False)
            new_user.set_password(user_register_form.cleaned_data["password"])
            new_user.save()
            login(request, new_user)
            return redirect(reverse("home:index"))
        else:
            return HttpResponse("注册表单输入有误, 请重新输入。")
    elif request.method == "GET":
        user_register_form = UserRegisterForm()
        context = {"form": user_register_form}
        return render(request, "accounts/templates/register.html", context)
    else:
        return HttpResponse("请使用GET或POST请求数据")
