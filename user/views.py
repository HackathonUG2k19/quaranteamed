
from .forms import RegisterForm,LoginForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .models  import Profile, Notif
from django.contrib.auth.decorators import login_required

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
@login_required
def notifications(request):
    notifs = Notif.objects.filter(user_reciever = request.user)
    context ={
        'notifs':notifs
    }
    return render(request,"notifications.html",context)
@login_required(login_url = "user:login")
def editprofile(request):

    profile = request.user.profile

    form = ProfileForm(request.POST or None,request.FILES or None,instance = profile)
    if form.is_valid():
        profile = form.save(commit=False)
        
        profile.user = request.user
        profile.save()

        messages.success(request," updated successfully")
        return redirect("user:profile",request.user)


    return render(request,"editprofile.html",{"form":form})