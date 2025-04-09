import importlib
from django.urls import path

from kitchen.views import index
from kitchen.models import BaseModelMixin, Dish, DishType, Ingredient

module_name = "kitchen.views"
module = importlib.import_module(module_name)


def create_urls(model: type[BaseModelMixin]):
    class_name = model.__name__
    list_view = getattr(module, class_name + "ListView").as_view()
    create_view = getattr(module, class_name + "CreateView").as_view()
    update_view = getattr(module, class_name + "UpdateView").as_view()
    result = [
        path(model.route + "/list/", list_view, name=model.route + "-list"),
        path(model.route + "/create/", create_view, name=model.route + "-create"),
        path(model.route + "/update/<int:pk>/", update_view, name=model.route + "-update"),
    ]

    return result

urlpatterns = [
    path("", index, name="index"),
]
urlpatterns += create_urls(Dish)
urlpatterns += create_urls(DishType)
urlpatterns += create_urls(Ingredient)

app_name = "kitchen"
