import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
django.setup()
os.getcwd()
# 'D:\\Chứng khoán\\Python\\Django\\myweb'
from myapp.models import Place, Restaurant  
print(Place.objects.all())
Restaurant.objects.all()
place = Place(name="Ben thanh market", address ="Quan 1", country ="Viet Nam")
place.save()
place1 = Place.objects.create(name ="Ha Noi square", address ="Quan 1", country="Viet Nam")
place_id1 = Place.objects.get(id=1)
rest1 = Restaurant.objects.get(place_id=place_id1.id)




