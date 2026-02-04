from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def error_404(request, exception):
    return render(request, '404page.html', status=404)