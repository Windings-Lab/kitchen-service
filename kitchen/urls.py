from django.urls import path

from kitchen.views import index, DishListView, DishCreateView

urlpatterns = [
    path("", index, name="index"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
]

app_name = "kitchen"
