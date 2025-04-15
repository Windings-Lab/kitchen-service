from functools import wraps
from io import BytesIO

import inflect
from django.contrib.auth.models import AbstractUser
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse
from PIL import Image
from utility import create_route
from django.urls.exceptions import NoReverseMatch


p = inflect.engine()


def handle_no_reverse_match(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoReverseMatch:
            return "#"
    return wrapper


class BaseModelMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        cls.route = create_route(cls.__name__)
        cls.class_name = cls.__name__
        cls.page_name = cls.route + "-page"
        cls.plural_name = (
            p.plural(cls.class_name.lower())
             .replace(" ", "")
        )


    @handle_no_reverse_match
    def get_create_url(self):
        url = "kitchen:" + self.route + "-create"

        return reverse(url)

    @handle_no_reverse_match
    def get_update_url(self):
        url = "kitchen:" + self.route + "-update"

        return reverse(url, kwargs={"pk": self.id})

    @handle_no_reverse_match
    def get_detail_url(self):
        url = "kitchen:" + self.route + "-detail"

        return reverse(url, kwargs={"pk": self.id})

    def save(self, *args, **kwargs):
        if hasattr(self, "image") and self.image:
            img = Image.open(self.image)
            img.thumbnail((300, 300))

            buffer = BytesIO()
            img.save(buffer, format=img.format or "PNG")
            buffer.seek(0)

            self.image.save(self.image.name, ContentFile(buffer.read()), save=False)

        super().save(*args, **kwargs)


class Cook(BaseModelMixin, AbstractUser):
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
