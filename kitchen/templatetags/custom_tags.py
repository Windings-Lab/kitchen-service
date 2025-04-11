from django import template
from functools import reduce

from django.db.models import QuerySet


from kitchen.models import BaseModelMixin
from utility import split_by_capitals

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
def get_errors(form, error_dict_name: str):
    return form.errors.get(error_dict_name.lower(), [])


@register.filter
def get_class_name(value):
    return " ".join([
        item.lower()
        for item in split_by_capitals(value.__class__.__name__)
    ])


@register.filter
def vowel_a_an(first_str, text: str):
    result = first_str + ("an" if text[0].lower() in "aeiou" else "a")
    return result


@register.simple_tag(takes_context=True)
def query_transform(context, **kwargs):
    request = context.get("request")
    if not request:
        return ""

    updated = request.GET.copy()
    for key, value in kwargs.items():
        if value is not None:
            updated[key] = value
        else:
            updated.pop(key, 0)

    result = updated.urlencode()
    return result
