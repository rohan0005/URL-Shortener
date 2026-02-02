from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login') # only logged in users can access this page, if user is not logged in then redirect to login page
def shortUrl(request):
    return render(request,"shorturl.html")
