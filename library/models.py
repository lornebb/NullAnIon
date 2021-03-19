from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_friendly_name(self):
        return self.friendly_name

class Song(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    category_secondary = models.CharField(max_length=254, null=True, blank=True)
    song_name = models.CharField(max_length=254)
    album_name = models.CharField(max_length=254, null=True, blank=True)
    artist_name = models.CharField(max_length=254, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    audio_link = models.URLField(max_length=1024)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.song_name
