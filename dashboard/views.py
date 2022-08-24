from django.shortcuts import render
from .models import Movie, Series
from bs4 import BeautifulSoup
import requests
import json

def index(request):
    if request.method == 'POST':
        # pass form url
        url = request.POST.get('imdb_url')
        r = requests.get(url)
        # extract relevant data
        soup = BeautifulSoup(r.content, features='html.parser')
        data = json.loads(soup.find('script', type='application/ld+json').text)
        # save to database
        if data['@type'] == 'Movie':
            new_movie = Movie(
                title = data['name'],
                poster = data['image'],
                imdb_URL = 'https://www.imdb.com%s' % data['url']
                )
            new_movie.save()
        elif data['@type'] == 'TVSeries':
            new_series = Series(
                title = data['name'],
                poster = data['image'],
                imdb_URL = 'https://www.imdb.com%s' % data['url']
                )
            new_series.save()
    try:
        return render(request, 'index.html', {'movies': Movie.objects.all(), 'tvseries': Series.objects.all()})
    except:
        return render(request, 'index.html')
