from django import template
from functools import reduce

from django.db.models import QuerySet

from kitchen.models import BaseModelMixin

register = template.Library()

@register.filter
def get_attribute(obj, attr_path):
    """Allows {{ obj|get_attribute:'field.subfield.subsubfield' }}"""
    try:
        result = reduce(getattr, attr_path.split("."), obj)
        return result
    except AttributeError:
        return ""


@register.filter
def get_query(obj, query_str):
    try:
        return obj.fields[query_str].queryset
    except Exception:
        return ""


@register.filter
def is_in_query(query: QuerySet, item):
    return query.filter(id=item.id).exists()


@register.filter
def get_errors(form, error_dict_name):
    return form.errors.get(error_dict_name, [])


@register.filter
def get_update_url(model_instance: BaseModelMixin):
    return model_instance.get_update_url()


@register.filter
def get_create_url(model_instance: BaseModelMixin):
    return model_instance.get_create_url()
