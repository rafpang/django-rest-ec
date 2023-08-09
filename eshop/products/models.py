from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.TextChoices):
    ELECTRONICS = "Electronics"
    LAPTOPS = "Laptops"
    ARTS = "Arts"
    FOOD = "Food"
    HOME = "Home"
    KITCHEN = "Kitchen"


class Product(models.Model):
    id = models.UUIDField()
    name = models.CharField(default="", blank=False, max_length=255)
    description = models.TextField(max_length=1000, default="", blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    category = models.CharField(max_length=30, choices=Category.choices)
    ratings = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    stock = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
