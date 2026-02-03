from django.urls import path
from shorturl import views

urlpatterns = [
    path('short-url', views.shortUrl, name='short-url'),
    
    
    
    path("<str:short_key>/", views.redirect_short_url, name="redirect"),

]