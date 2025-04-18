from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishForm
from kitchen.models import Dish, DishType, Ingredient, Cook


class SearchMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_value"] = self.request.GET.get("search_value", "")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_value = self.request.GET.get("search_value")
        search_field = self.request.GET.get("search_field") or "name"

        if search_value:
            lookup = f"{search_field}__icontains"
            queryset = queryset.filter(**{lookup: search_value})

        return queryset


def index(request):
    """View function for the home page of the site."""
    return render(request, "kitchen/index.html")


class CookListView(SearchMixin, generic.ListView):
    model = Cook
    paginate_by = 5


class DishTypeListView(SearchMixin, generic.ListView):
    model = DishType
    template_name = "kitchen/default_list.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        context["title"] = "Dish Types"
        return context


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/card_form.html"


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")
    template_name = "kitchen/card_form.html"


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "kitchen/card_detail.html"


class DishListView(SearchMixin, generic.ListView):
    model = Dish
    template_name = "kitchen/default_list.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(DishListView, self).get_context_data(**kwargs)
        context["title"] = "Dishes"
        return context


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context[DishType.plural_name] = DishType.objects.only("name")
        context[Ingredient.plural_name] = Ingredient.objects.only("name")
        context[Cook.plural_name] = Cook.objects.only("username")

        return context


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")

    def get_queryset(self):
        query = super().get_queryset()
        query = query.select_related("dish_type").only(
            "name",
            "description",
            "price",
            "image",
            "dish_type__name",
        )
        query = query.prefetch_related(
            Prefetch("ingredients", queryset=Ingredient.objects.only("name")),
            Prefetch("cooks", queryset=Cook.objects.only("username")),
        )

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dish = self.object

        context[DishType.plural_name] = DishType.objects.only("name")

        return context



class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish

    def get_queryset(self):
        query = super().get_queryset()
        query = query.select_related("dish_type").only(
            "name",
            "description",
            "price",
            "image",
            "dish_type__name",
        )

        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        dish = self.object

        context[Ingredient.plural_name] = dish.ingredients.only("name")
        context[Cook.plural_name] = dish.cooks.only("username")

        return context


class IngredientListView(SearchMixin, generic.ListView):
    model = Ingredient
    template_name = "kitchen/default_list.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(IngredientListView, self).get_context_data(**kwargs)
        context["title"] = "Ingredients"
        return context


class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/card_form.html"


class IngredientUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kitchen/card_form.html"


class IngredientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ingredient
    template_name = "kitchen/card_detail.html"
