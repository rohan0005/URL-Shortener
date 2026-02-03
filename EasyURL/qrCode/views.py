from django.shortcuts import render
import qrcode
from shorturl.models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from io import BytesIO

# Create your views here.
def qr_code(request,short_key):
    obj = get_object_or_404(ShortUrl, short_key=short_key)
    
    qr = qrcode.make(obj.short_url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    
    return HttpResponse(buffer.getvalue(), content_type="image/png")