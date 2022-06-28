import os
import sys
import django
from django.utils.timezone import now
import requests
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
django.setup()
from myapp.models import Article, Source
http_request = requests.get("https://gnews.io/api/v4/top-headlines?token=6cb3c9110b9e039e90ffeabcd4c5166d&lang=e")
data = http_request.json()
for article in data['articles'][:10]:
    new_article = Article.objects.create(
    title = article['title'],
    url = article['url'],
    image = article['image'],
    published_date = '15-12-2021',

    )
    Source.objects.create(
        article=new_article,
        name = article['source']['name'],
        url = article['source']['url'],
    )