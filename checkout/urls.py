from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout-complete/', views.checkout_complete, name='checkout-complete'),
]
