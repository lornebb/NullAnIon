from django.urls import path
from . import views

urlpatterns = [
    # path('', views.checkout, name='checkout'),
    path('checkout/', views.checkout_order_mix, name='checkout_order_mix'),
    path('checkout/', views.checkout_order_master, name='checkout_order_master'),
    path('checkout/', views.checkout_order_production, name='checkout_order_production')
]
