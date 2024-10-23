from . import Check, Finding
from .utils import is_index, get_module, get_first_heading


class TopLevelCasingFinding(Finding):
    NAME = "TopLevelCasing"

    def msg(self):
        return "Module name has wrong case"


class TopLevelCasingCheck(Check):
    FINDING = TopLevelCasingFinding

    def run(self, file, lines):
        if not is_index(file):
            return
        module = get_module(file)
        top_level_heading, i = get_first_heading(lines)
        if top_level_heading and top_level_heading.lower().startswith(module.lower()):
            if not top_level_heading.startswith(module):
                self.add_finding(file, i + 1)
