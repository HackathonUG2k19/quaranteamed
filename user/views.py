from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"Registered Successfully")

        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Username or password is incorrect")
            return render(request,"login.html",context)

        messages.success(request,"Successfully logged in.")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("index")


def settingUser(request):
    if request.user.is_authenticated:
        form = None
        if request.method == "POST":
            form=PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                # user = form.save()
                update_session_auth_hash(request,form.request.user)
        user_info = User(user=request.user)
        context = { 'user_info' : user_info,
                    'form' : form }
        messages.success(request,"Password successfully changed")
        return render(request,"dashboard.html",context)

    return redirect("index")

