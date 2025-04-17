from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Case, When, BooleanField, Value

from kitchen.models import Dish, Ingredient


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"

    # noinspection PyTypeChecker
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["ingredients"] = forms.ModelMultipleChoiceField(
            queryset=Ingredient.objects.only("name").annotate(
                selected=Case(
                    When(
                        id__in=self.instance.ingredients.values("id"),
                        then=Value(True)
                    ),
                    default=Value(False),
                    output_field=BooleanField()
                )
            ).order_by("-selected"),
            widget=forms.CheckboxSelectMultiple
        )


        self.fields["cooks"] = forms.ModelMultipleChoiceField(
            queryset=get_user_model().objects.only("username").annotate(
                selected=Case(
                    When(
                        id__in=self.instance.cooks.values("id"),
                        then=Value(True)
                    ),
                    default=Value(False),
                    output_field=BooleanField()
                )
            ).order_by("-selected"),
            widget=forms.CheckboxSelectMultiple
        )

