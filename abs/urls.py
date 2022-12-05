from django.urls import path, include
from . import views

urlpatterns = [
    path('client/list/', views.client_list, name='client_list'),
    path('client/create/', views.client_form, name='client_insert'),
    path('client/update/<int:id>/', views.client_form, name='client_edit'),
    path('client/delete/<int:id>/', views.client_delete, name='client_delete'),
    path('product/list/', views.product_list, name='product_list'),
    path('product/create/', views.product_form, name='product_insert'),
    path('product/update/<int:id>/', views.product_form, name='product_edit'),
    path('product/delete/<int:id>/', views.product_delete, name='product_delete'),
    path('order/create/', views.product_qty, name='product_qty'),

]
