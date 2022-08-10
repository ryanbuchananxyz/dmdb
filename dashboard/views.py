from django.shortcuts import render
from .models import Title
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
        new_title = Title(
            title=data['name'],
            poster=data['image']
            )
        new_title.save()
    return render(request, 'index.html', {'titles': Title.objects.all()})