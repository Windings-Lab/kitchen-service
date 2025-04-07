from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from kitchen.models import Dish


def index(request):
    """View function for the home page of the site."""

    # num_drivers = Driver.objects.count()
    # num_cars = Car.objects.count()
    # num_manufacturers = Manufacturer.objects.count()
    #
    # num_visits = request.session.get("num_visits", 0)
    # request.session["num_visits"] = num_visits + 1
    #
    # context = {
    #     "num_drivers": num_drivers,
    #     "num_cars": num_cars,
    #     "num_manufacturers": num_manufacturers,
    #     "num_visits": num_visits + 1,
    # }

    return render(request, "kitchen/index.html")


class DishListView(generic.ListView):
    model = Dish

    def get_context_data(self, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        context["create_dish_url"] = reverse("kitchen:dish-create")
        return context


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")

