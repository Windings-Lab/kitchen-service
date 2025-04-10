from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.apps import apps


class DeleteItemView(generic.View):
    def post(self, request, *args, **kwargs):
        # Get the model name and item ID from the POST data
        class_name = request.POST.get("class_name")
        item_id = request.POST.get("item_id")

        # Dynamically fetch the model class using the model name
        # TODO: Replace hardcoded app_label
        model_class = apps.get_model("kitchen", class_name)

        # Fetch the item using the dynamically loaded model
        item = get_object_or_404(model_class, id=item_id)

        # Delete the item
        item.delete()

        # Redirect to a success page or back to the item list
        return redirect(request.META.get("HTTP_REFERER"))
