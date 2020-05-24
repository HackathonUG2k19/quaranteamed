
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .models  import Profile, Notif
# Create your views here.

def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username =username)
        newUser.set_password(password)


        newUser.save()
        new_profile = Profile(user=newUser)
        new_profile.save()
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

def  profile(request, name):
    obj = get_object_or_404(User,username=name)
    prof= get_object_or_404(Profile, user=obj)
    context={
        "profile":prof
    }
    return render(request,"profile.html",context)

