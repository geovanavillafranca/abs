from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=25, blank=False, unique=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    last_update = models.DateTimeField(auto_now=True)

