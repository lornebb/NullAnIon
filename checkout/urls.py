from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('checkout_complete/<order_number>',
         views.checkout_complete,
         name='checkout_complete'),
    path('checkout_complete_production/<order_number>',
         views.checkout_complete_production,
         name='checkout_complete_production'),
    path('wh/', webhook, name="webhook"),
    path('checkout_production',
         views.checkout_production,
         name="checkout_production")
]
