from django.urls import path, include
from . import views

urlpatterns = [
    path('client/list/', views.client_list, name='client_list'),
    path('client/create/', views.client_form, name='client_insert'),
    path('client/update/<int:id>/', views.client_form, name='client_edit'),
    path('client/delete/<int:id>/', views.client_delete, name='client_delete')
]
