from datetime import datetime
from time import time
from django.db import models
from django.utils import timezone
from more_itertools import quantify
# Create your models here.

class User(models.Model):
    """It is the user model with its respective attributes

    Args:
        models (models):A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing
    """
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255 , unique = True) 
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    type_user =models.CharField(max_length=20)


class Product(models.Model):
    """It is the Product model with its respective attributes

    Args:
        models (models):A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing
    """
    id =models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20)
    type_product= models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    stock =models.IntegerField(null=True, blank=True)
    dateAdded = models.DateField(default=datetime.today)
    image = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True, blank=True)