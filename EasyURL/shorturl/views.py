from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from EasyURL.utils import *
from datetime import timedelta
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseGone



# Create your views here.

@login_required(login_url='login') # only logged in users can access this page, if user is not logged in then redirect to login page
def shortUrl(request):
    SALT = 1000000
    
    shortUrl = None
    
    if request.method == "POST":
        original_url = request.POST.get('user_url')
        expire_time = request.POST.get('expire_time')  
        #expire_time = None
        user = request.user
        object = ShortUrl.objects.create(original_url=original_url, user=user)
        object.save()
        
        #generating short url key
        object.short_key = encode_base62(object.id + SALT)
        
        
        #short url with absolute url
        short_url = request.build_absolute_uri(f"/{object.short_key}")
        object.short_url=short_url
        
        #expire time
        if expire_time:
            object.expiry_date = timezone.now() + timedelta(hours=int(expire_time))

        
        #save in database
        object.save()
        print("success")
    
        return render(request, "shorturl.html", {"short_url": short_url})

        
    return render(request,"shorturl.html")




def redirect_short_url(request, short_key):
    object = get_object_or_404(ShortUrl,short_key=short_key)
    
    if object.is_expired():
        return HttpResponseGone("This short URL has expired.")
    
    return redirect(object.original_url)


    