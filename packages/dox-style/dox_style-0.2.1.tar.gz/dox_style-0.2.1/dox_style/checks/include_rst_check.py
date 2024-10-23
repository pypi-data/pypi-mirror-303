from . import Check, Finding
import re


class IncludeRstFinding(Finding):
    NAME = "IncludeRst"

    def msg(self):
        return "Include-directive must not point to an *.rst file"


class IncludeRstCheck(Check):
    FINDING = IncludeRstFinding

    include_rst_regex = re.compile(r"\.\.\s+include\s*::.*\.rst$")

    def run(self, file, lines):
        for i, line in enumerate(lines):
            if self.include_rst_regex.match(line):
                self.add_finding(file, i + 1)
