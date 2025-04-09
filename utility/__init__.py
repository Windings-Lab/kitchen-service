import re

def split_by_capitals(text):
    # Regular expression to match capitalized words
    return re.findall(r'[A-Z][a-z]*', text)


def create_route(class_name: str):
    return "-".join([
            item.lower()
            for item in split_by_capitals(class_name)
        ])
