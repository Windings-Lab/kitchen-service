from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField()


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    dish_type = models.ForeignKey(
        DishType, on_delete=models.SET_NULL, related_name="dishes"
    )
    cooks = models.ManyToManyField(Cook, related_name="dishes")
