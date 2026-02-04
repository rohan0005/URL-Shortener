from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from EasyURL.utils import *
from datetime import timedelta
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseGone
from django.contrib import messages




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
    
        return render(request, "shorturl.html", {"short_url": short_url, "short_key": object.short_key})

        
    return render(request,"shorturl.html")



#redirecting short url to original url
def redirect_short_url(request, short_key):
    object = get_object_or_404(ShortUrl,short_key=short_key)
    
    if object.is_expired():
        return HttpResponseGone("This short URL has expired.")
    
    # incrementing click count
    object.clicks +=1
    object.save()
    
    return redirect(object.original_url)

@login_required(login_url='login')
def edit_url(request, short_key):
    object = get_object_or_404(ShortUrl, short_key=short_key, user=request.user)
    
    if request.method == "POST":
        new_short_key = request.POST.get('new_short_key')

        #if empty;
        if not new_short_key:
            messages.error(request, 'Short key cannot be empty!')
            return redirect('dashboard')
        
        # onlt alphanumeric
        if not new_short_key.isalnum():
            messages.error(request, 'Only letters and numbers are allowed in short key!')
            return redirect('dashboard')

        # if user save without changing
        if new_short_key == short_key:
            messages.info(request, 'No changes detected.')
            return redirect('dashboard')
        
        #uniqe url check
        if ShortUrl.objects.filter(short_key=new_short_key).exists():
            messages.error(request, 'This short key is already exist. Please choose another one.')
            return redirect('dashboard')

        #if all conditions are satisfied then saving the new short key
        object.short_key = new_short_key
        object.short_url = request.build_absolute_uri(f"/{new_short_key}")
        object.save()
        messages.success(request, 'Short URL updated successfully!')
        
    return redirect('dashboard')

@login_required(login_url='login')
def delete_url(request, short_key):
    object = get_object_or_404(ShortUrl, short_key=short_key, user=request.user)
    
    if request.method == "POST":
        object.delete()
        messages.success(request, 'Short URL deleted successfully!')
    return redirect('dashboard')
    
