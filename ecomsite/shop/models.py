from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    discount_price=models.FloatField()
    category=models.CharField(max_length=100)
    description=models.TextField()
    image=models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    order=models.CharField(max_length=10,editable=False)
    items=models.CharField(max_length=1000)
    total=models.FloatField(default=0)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    address2=models.CharField(max_length=1000)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.order