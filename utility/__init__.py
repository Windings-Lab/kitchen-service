import re

from django.core.paginator import Paginator
from django.db.models import QuerySet


def split_by_capitals(text):
    # Regular expression to match capitalized words
    return re.findall(r'[A-Z][a-z]*', text)


def create_route(class_name: str):
    return "-".join([
            item.lower()
            for item in split_by_capitals(class_name)
        ])


def create_pagination(
        queryset: QuerySet,
        page_num: int = 1
) -> dict:
    context = {}
    paginator = Paginator(queryset, 5)
    page = paginator.page(page_num)
    context["paginator"] = paginator
    context["page_obj"] = page
    context["is_paginated"] = page.has_other_pages()
    context["object_list"] = page.object_list
    context["page_name"] = queryset.model.page_name

    return context
