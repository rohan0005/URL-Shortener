from django.urls import path
from . import views

urlpatterns = [
    path('qr/<str:short_key>/', views.qr_code, name='qr-code'),
]
