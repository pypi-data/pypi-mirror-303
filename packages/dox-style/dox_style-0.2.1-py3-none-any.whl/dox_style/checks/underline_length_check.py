from . import Check, Finding
from .utils import is_heading


class UnderlineLengthFinding(Finding):
    NAME = "UnderlineLength"

    def msg(self):
        return f"Heading underline length does not match title length"


class UnderlineLengthCheck(Check):
    FINDING = UnderlineLengthFinding

    def run(self, file, lines):
        prev_line_length = -1

        for i, line in enumerate(lines):
            line_length = len(line)
            if is_heading(line) and prev_line_length != line_length and prev_line_length != -1:
                self.add_finding(file, i + 1)

            prev_line_length = line_length
