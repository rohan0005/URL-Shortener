from django.urls import path
from shorturl import views

urlpatterns = [
    path('short-url', views.shortUrl, name='short-url'),
    
    
    
    path("<str:short_key>/", views.redirect_short_url, name="redirect"),
    path('edit/<str:short_key>/', views.edit_url, name='edit-url'),
    path('delete/<str:short_key>/', views.delete_url, name='delete-url'),  # ✅ Add this

]