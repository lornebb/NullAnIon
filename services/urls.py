from django.urls import path
from . import views

urlpatterns = [
    path('order', views.order_form, name='services'),
    path('production_order', views.production_order, name='production_order'),
]
