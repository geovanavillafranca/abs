from django.db import models
from .product import Product
from .client import Client

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0, blank=False)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    delivery_forecast = models.DateField(blank=True, null=True)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20, blank=True)
    is_paid = models.BooleanField(default=False)
    order_items = models.ManyToManyField(OrderItem)
    total_pay = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)


