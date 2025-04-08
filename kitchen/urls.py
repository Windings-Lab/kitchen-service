from django.urls import path

from kitchen.views import index, DishListView, DishCreateView, \
    DishTypeCreateView
from views import DishTypeListView

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dish-type/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-type/create/", DishTypeCreateView.as_view(),
         name="dish-type-create"),
]

app_name = "kitchen"
