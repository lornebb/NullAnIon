from django.contrib import admin
from .models import Mix, Master, Production

# Register your models here.
admin.site.register(Mix)
admin.site.register(Master)
admin.site.register(Production)