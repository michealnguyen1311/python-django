import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')
django.setup()
from myapp.models import Place, Restaurant, Waiter

place1= Place.objects.get(pk=1)
print(place1)
restaurant = place1.restaurant
print(restaurant)
waiters = restaurant.waiter_set.all()
print(waiters)
waiter1 = Waiter(name="Justin", restaurant_id= restaurant.place_id)
waiter1.save()

waiter2= Waiter(name="Justin 1", restaurant= restaurant)
waiter2.save()

waiter3 = Waiter.objects.create(name="Justin 2", restaurant= restaurant)
restaurant.waiter_set.create(name="Justin 2")