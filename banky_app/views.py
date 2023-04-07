from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *

# Create your views here.

def home(request):
    card = Card.objects.filter()[0:4]
    return render(request, 'home.html', {'card':card})


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form':form})


def details(request, pk):
    card = get_object_or_404(Card, pk=pk)
    return render(request, 'details.html',  {'card':card})

def more(request ):
    card = Card.objects.all()
    return render(request, 'more.html',  {'card':card})


def about (request):
    card = Card.objects.all()
    return render(request, "about.html",{'card':card})

def service (request):
    card = Card.objects.all()
    return render(request, "services.html",{'card':card})


def withdraw (request):
    return render(request, "withdraw.html")


def contact (request):
    card = Card.objects.filter()[0:4]
    return render(request, 'contact.html', {'card':card})


def login_form(request):
    if(request.method =="POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
                if user.is_active:
                    login(request,user)
                    messages.info(request,'successful logged in as {username}')
                    return HttpResponseRedirect('/dashboard')
                else:
                    return HttpResponse(request,'User not active')
        else:
            return HttpResponse(request, "your details are incorrect")
    else:
        return render(request, "login.html",)
        
@login_required(login_url='/login')
def dashboard(request):
    profile = Profile.objects.all()
    rActivity = rActivities.objects.all()[0:4]
    if request.method == "POST":
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, "index.html", {'profile':profile,"rActivity":rActivity})

def transactions(request):
    rActivity = rActivities.objects.all()
    return render(request,"transactions.html", {'rActivity':rActivity})

def profile(request):
    # profile = Profile.objects.all()'profile':profile
    if request.method == "POST":
        form = UserProfile(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')
    else:
        form = UserProfile()
    return render(request, "profile.html", {"form":form,})

def logout_view(request):
    logout(request)
    return redirect('/login')

def notFound(request):
    return render(request,'404.html')

