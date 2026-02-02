from django.urls import path
from shorturl import views

urlpatterns = [
    path('short-url', views.shortUrl, name='short-url'),
    
]