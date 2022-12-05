from django import template
from ..models import *

register = template.Library()

@register.filter(name='product_price_total')
def product_price_total(product):
    total = product.product.price * product.qty
    prod = OrderItem.objects.get(pk=product.id)
    prod.price = total
    prod.save()
    return total

@register.filter(name='order_price_total')
def order_price_total(products):
    sum = 0
    for p in products:
        sum += p.price
    return sum