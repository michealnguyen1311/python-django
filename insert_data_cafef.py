import os
import sys
import django
from django.utils.timezone import now
import requests
import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
django.setup()
from myapp.models import CafefArticle
http_request = requests.get("http://news.moneyclub.vn/news?page=0&size=10")
data = http_request.json()
for article in data:
    new_article = CafefArticle.objects.create(
    title = article['title'],
    url = article['url'],
    )
