from django.urls import path

from kitchen.views import index, DishListView, DishCreateView, \
    DishTypeCreateView, IngredientListView, IngredientCreateView
from views import DishTypeListView

urlpatterns = [
    path("", index, name="index"),
    path("dish/list", DishListView.as_view(), name="dish-list"),
    path("dish/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish-type/list", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-type/create/", DishTypeCreateView.as_view(),
         name="dish-type-create"),
    path("ingredient/list", IngredientListView.as_view(),
         name="ingredient-list"),
    path("ingredient/create/", IngredientCreateView.as_view(),
         name="ingredient-create"),
]

app_name = "kitchen"
