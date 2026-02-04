from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from shorturl.models import ShortUrl
from django.contrib.auth.decorators import login_required

from .forms import *

# Create your views here.
def loginUser(request):
    
    if request.user.is_authenticated: return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        
        #checking if user exists 
        if user is not None:
            # checking if user is admin or not
            #CODE
            
            login(request, user)
            print("Login Successful")
            return redirect('home')
                
    
    
    return render(request, "Authentication/login.html")


def registerUser(request):
    if request.user.is_authenticated: return redirect('home')

    try:
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully Registered! Please Login!')
                return redirect('login')
    
    except Exception as e:
        print(e)
        
        return redirect('register')
    
    return render(request, "Authentication/register.html")


def logoutUser(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('login')

@login_required(login_url='login')
def UserDashboard(request):
    
    user = request.user
    
    URLDetails = ShortUrl.objects.filter(user=user)
    
    print(URLDetails)
    
    context = {
        "URLDetails": URLDetails
    }
    
    return render(request, "dashboard.html", context)