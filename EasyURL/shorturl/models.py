from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ShortUrl(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    original_url = models.URLField()
    short_url = models.CharField(unique=True, max_length=100, blank=True, null=True)
    short_key = models.CharField(unique=True, max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(null=True, blank=True)
    
    def is_expired(self):
        if self.expiry_date is None:
            return False
        return timezone.now()>self.expiry_date
    
    
    def __str__(self):
        return str(self.short_key)
