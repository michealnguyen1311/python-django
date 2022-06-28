import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
django.setup()
from  myapp.models import Place, Restaurant

keyword = input("hay nhap tu khoa can tim:")
matched_place = Place.objects.filter(name__contains=keyword)
matched_restaurant = Restaurant.objects.filter(place__name__contains=keyword)
print("ds")
for place in matched_place:
    print("{0:>5}{1:>20}{2:>20}".format(place.id, place.name, place.address))
print("ds restaurant")
for restaurant in matched_restaurant:
    print(restaurant)