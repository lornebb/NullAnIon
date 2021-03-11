from django.urls import path
from . import views

urlpatterns = [
    path('mix', views.mix_form, name='services-mix'),
    path('master', views.master_form, name='services-master'),
    path('production', views.production_form, name='services-production'),
]
