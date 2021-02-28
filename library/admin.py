from django.contrib import admin
from .models import Song, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Song)
