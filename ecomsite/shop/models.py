from unicodedata import category
from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    discont_price=models.FloatField()
    category=models.CharField(max_length=100)
    description=models.TextField()
    image=models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name