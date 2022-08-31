from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True,auto_created=True)
    imageUrl = models.CharField(max_length=500)
    name = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=1,max_digits=4)
    rating = models.DecimalField(decimal_places=1,max_digits=4)
    producer = models.CharField(max_length=250) #Create a many to one relationship FK (Producers)
    unit = models.CharField(max_length=50) #Create a many to one relationship FK (Sys Meta >Measure_Units)
    category = models.CharField(max_length=100) #Create a many to one relationship FK (Sys <eta >Categories)
    isFeatured = models.BooleanField()
