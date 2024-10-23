from . import Check, Finding
import re


class TrailingWhitespacesFinding(Finding):
    NAME = "TrailingWhitespace"

    def msg(self):
        return f"Line contains trailing whitespaces"


class TrailingWhitespacesCheck(Check):
    FINDING = TrailingWhitespacesFinding

    trailing_whitespace_regex = re.compile(r".*\s+$")

    def run(self, file, lines):
        for i, line in enumerate(lines):
            if self.trailing_whitespace_regex.match(line):
                self.add_finding(file, i + 1)
