from django.db import models
from django.db.models.base import Model

# Create your models here.
class Place(models.Model):
    name = models.CharField(verbose_name="Tên địa điểm", max_length=50)
    address = models.CharField(verbose_name="Địa chỉ", max_length=100)
    country = models.CharField(verbose_name="Quốc Gia", max_length=100, default="Viet Nam")

    def __str__(self):
        return f"{self.name}"
        
    class Meta:
        db_table = "Place"

class Restaurant(models.Model):
    place = models.OneToOneField(
    Place,
    on_delete= models.CASCADE,
    primary_key=True
    )
    serves_hot_dogs = models.BooleanField(verbose_name="Phục vụ Hot Dog", default=False)
    serves_pizza = models.BooleanField(verbose_name="Phục vụ Pizza", default=False)
    serves_pho = models.BooleanField(verbose_name="Phục vụ Phở", default=True)

    def __str__(self):
        return f"{self.place.name}"
    
    class Meta:
        db_table = "Restaurant"

class Waiter(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
    
    )
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name} is a waiter at {self.restaurant}"
    class Meta:
        db_table = "Waiter"
class Publication(models.Model):
    title = models.CharField(max_length=100)
    # articles = models.ManyToManyField("Article")
    class Meta:
        db_table = "Publication"
    def __str__(self):
        return f"{self.title} is a Publication"


class Article(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    published_date = models.DateField()
    class Meta:
        db_table="Article"

class Source(models.Model):
    article = models.OneToOneField(Article,
        primary_key=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    class Meta:
        db_table="Source"

class CafefArticle(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    tag = models.TextField(max_length=20)
    class Meta:
        db_table="CafefArticle"




    

    