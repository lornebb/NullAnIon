from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout/', views.checkout_order, name='checkout_order')
]
