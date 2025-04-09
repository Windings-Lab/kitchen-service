from django import template
from functools import reduce

from kitchen.models import BaseModelMixin

register = template.Library()

@register.filter
def get_attribute(obj, attr_path):
    """Allows {{ obj|get_attribute:'field.subfield.subsubfield' }}"""
    try:
        return reduce(getattr, attr_path.split("."), obj)
    except AttributeError:
        return ""


@register.filter
def get_query(obj, query_str):
    try:
        return obj.fields[query_str].queryset
    except Exception:
        return ""


@register.filter
def get_update_url(model_instance: BaseModelMixin):
    return model_instance.get_update_url()


@register.filter
def get_create_url(model_instance: BaseModelMixin):
    return model_instance.get_create_url()
