from django.contrib.auth.models import AbstractUser
from django.db import models


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)


class DishType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(
        upload_to="dish_type/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(
        upload_to="ingredient/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to="dish/",
        null=True,
        blank=True,
    )
    dish_type = models.ForeignKey(
        DishType,
        null=True,
        on_delete=models.SET_NULL,
        related_name="dishes"
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name="dishes",
    )
    cooks = models.ManyToManyField(
        Cook,
        related_name="dishes"
    )
