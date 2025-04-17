import re

from django.core.paginator import Paginator
from django.db.models import QuerySet


def split_by_capitals(text):
    """
    Splits a given string into a list of words based on capitalized letters. Each word
    starts with an uppercase letter followed by any number of lowercase letters.

    :param text: Input string to be split.
    :type text: str
    :return: A list of words derived from the input string, where each word starts
        with an uppercase letter followed by lowercase letters.
    :rtype: list[str]
    """
    return re.findall(r'[A-Z][a-z]*', text)


def create_route(class_name: str):
    """
    Generate a route string by splitting a given class name into words.

    Creates a URL-friendly, lowercase string by splitting the input class
    name into separate words wherever a capital letter is encountered, then
    joining these words with hyphens.

    :param class_name: The input class name to transform into a route string.
    :type class_name: str
    :return: A URL-friendly, hyphenated, lowercase string derived from the
        given class name.
    :rtype: str
    """
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
