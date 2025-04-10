from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from PIL import Image
from utility import create_route


class BaseModelMixin:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        cls.route = create_route(cls.__name__)

    def get_create_url(self):
        url = "kitchen:" + self.route + "-create"

        return reverse(url)

    def get_update_url(self):
        url = "kitchen:" + self.route + "-update"

        return reverse(url, kwargs={"pk": self.id})

    def get_detail_url(self):
        url = "kitchen:" + self.route + "-detail"

        return reverse(url, kwargs={"pk": self.id})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save original image

        if self.image:
            img_path = self.image.path
            img = Image.open(img_path)

            # Resize logic
            max_size = (400, 400)  # Thumbnail size
            img.thumbnail(max_size)

            img.save(img_path)  # Overwrite the original


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=0)


class DishType(BaseModelMixin, models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(
        upload_to="dish_type/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Ingredient(BaseModelMixin, models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(
        upload_to="ingredient/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Dish(BaseModelMixin, models.Model):
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
