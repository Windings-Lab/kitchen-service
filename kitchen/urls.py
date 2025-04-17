import importlib
from django.urls import path

from kitchen.views import index
from kitchen.models import BaseModelMixin, Dish, DishType, Ingredient, Cook

module_name = "kitchen.views"
module = importlib.import_module(module_name)


def create_urls(model: type[BaseModelMixin]):
    class_name = model.__name__
    result = []

    try:
        list_view = getattr(module, class_name + "ListView").as_view()
        result.append(path(model.route + "/list/", list_view, name=model.route + "-list"))
    except AttributeError:
        pass

    try:
        create_view = getattr(module, class_name + "CreateView").as_view()
        result.append(path(model.route + "/create/", create_view, name=model.route + "-create"))
    except AttributeError:
        pass

    try:
        update_view = getattr(module, class_name + "UpdateView").as_view()
        result.append(path(model.route + "/update/<int:pk>/", update_view, name=model.route + "-update"))
    except AttributeError:
        pass

    try:
        detail_view = getattr(module, class_name + "DetailView").as_view()
        result.append(path(model.route + "/detail/<int:pk>/", detail_view, name=model.route + "-detail"))
    except AttributeError:
        pass

    return result

urlpatterns = [
    path("", index, name="index"),
]
urlpatterns += create_urls(Cook)
urlpatterns += create_urls(Dish)
urlpatterns += create_urls(DishType)
urlpatterns += create_urls(Ingredient)

app_name = "kitchen"
