from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.models import Dish, DishType, Ingredient


class SearchMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search_value", "")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_value = self.request.GET.get("search_value")

        if search_value:
            queryset = queryset.filter(name__icontains=search_value)

        return queryset


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


class DishTypeListView(SearchMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/default_list.html"

    def get_context_data(self, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        context["title"] = "Dish Types"
        return context


class DishTypeCreateView(generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/card_form.html"


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/card_form.html"


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "kitchen/card_detail.html"


class DishListView(SearchMixin, generic.ListView):
    model = Dish
    template_name = "kitchen/default_list.html"

    def get_context_data(self, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        context["title"] = "Dishes"
        return context


class DishCreateView(generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")


class DishDetailView(generic.DetailView):
    model = Dish


class IngredientListView(SearchMixin, generic.ListView):
    model = Ingredient
    template_name = "kitchen/default_list.html"

    def get_context_data(self, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        context["title"] = "Ingredients"
        return context


class IngredientCreateView(generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/card_form.html"


class IngredientUpdateView(generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/card_form.html"


class IngredientDetailView(generic.DetailView):
    model = Ingredient
    template_name = "kitchen/card_detail.html"
