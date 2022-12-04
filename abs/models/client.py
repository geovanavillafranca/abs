from django.db import models
from .zone import Zone

class Client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    company_name = models.CharField(max_length=80, blank=True)
    phone_number = models.CharField(max_length=14, blank=False, unique=True)
    address = models.CharField(max_length=120, blank=False)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=9, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)


        
