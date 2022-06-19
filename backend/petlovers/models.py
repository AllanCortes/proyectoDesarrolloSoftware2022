from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255 , unique = True) 
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    typeUser =models.CharField(max_length=20)


class Product(models.Model):
    id =models.AutoField(primary_key=True)
    productName = models.CharField(max_length=20)
    typeProduct = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=50,null=True)
    dateAdded = models.DateField(null=True)