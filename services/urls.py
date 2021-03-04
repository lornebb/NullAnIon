from django.urls import path
from . import views

urlpatterns = [
    path('', views.mix_form, name='services')
]
