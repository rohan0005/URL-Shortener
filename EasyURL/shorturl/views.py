from django.shortcuts import render

# Create your views here.

def shortUrl(request):
    return render(request,"shorturl.html")
