from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, redirect, HttpResponse

from .forms import UserLoginForm, UserSignupForm


def login_view(request):
    print (request.user.is_authenticated)
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/home/')
    return render(request, "accounts/Login.html", {"form": form,"title": title })

def signup_view(request):
    print (request.user.is_authenticated)
    title = "Signup"
    form = UserSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        return HttpResponse('User Register')
    context = {
        "form": form,
        "title": title
        }
    return render(request, "accounts/Signup.html", context)
def logout_view(request):
    logout(request)
    return redirect('login')




