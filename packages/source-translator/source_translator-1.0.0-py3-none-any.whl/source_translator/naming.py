import re


def snake_to_lower_camel(string):
    return re.sub("_[a-z]", lambda p: p.group(0)[1].upper(), string)
