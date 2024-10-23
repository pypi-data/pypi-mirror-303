import re
from typing import Union

heading_regex = re.compile(r"([=\-`:'\"~^_*+#<>])\1*$")
index_regex = re.compile(r".*/([^/]+)/doc/index.rst")


def is_heading(line: str) -> bool:
    return heading_regex.match(line) is not None


def is_index(file: str) -> bool:
    return index_regex.match(file) is not None


def get_module(file: str) -> Union[str, None]:
    match = index_regex.match(file)
    if match:
        return match.group(1)
    else:
        return None


def get_first_heading(lines):
    heading_candidate = None
    for i, line in enumerate(lines):
        if (
            is_heading(line)
            and heading_candidate is not None
            and len(line) >= len(heading_candidate)
        ):
            return heading_candidate
        heading_candidate = line, i
    return "", -1
