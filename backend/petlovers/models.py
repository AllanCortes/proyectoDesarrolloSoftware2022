from datetime import datetime
from time import time
from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    """Create the user model with all its attributes
    """
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255 , unique = True) 
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    type_user =models.CharField(max_length=20)


class Product(models.Model):
    """Create the Product model with all its attributes
    """
    id =models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20)
    type_product= models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    stock =models.IntegerField(null=True, blank=True)
    dateAdded = models.DateField(default=datetime.today)