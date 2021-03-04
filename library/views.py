from django.shortcuts import render
from .models import Song

# Create your views here.

def library(request):
    """ A view to return library page and songs from library """

    song = Song.objects.all()

    context = {
        'song': song,
    }

    return render(request, 'library/library.html', context)
    