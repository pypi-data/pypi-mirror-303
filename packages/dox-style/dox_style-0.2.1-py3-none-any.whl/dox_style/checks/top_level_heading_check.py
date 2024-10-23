from . import Check, Finding
from .utils import is_index, get_first_heading


class TopLevelHeadingFinding(Finding):
    NAME = "TopLevelHeading"

    def msg(self):
        return "Document has no heading"


class TopLevelHeadingCheck(Check):
    FINDING = TopLevelHeadingFinding

    def run(self, file, lines):
        if not is_index(file):
            return
        _, i = get_first_heading(lines)
        if i == -1:
            self.add_finding(file, 1)
