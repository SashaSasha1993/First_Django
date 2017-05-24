from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Song, Artist
from django.template import loader


# Create your views here.

def Index(request):
    html = "<h1>ALL ARTISTS</h1>"
    all_artists = Artist.objects.all()
    return HttpResponse(all_artists)
def Songs_page(request, song_name):
    html = "<h1>LIST OF SONGS</h1>" + str(song_name)
