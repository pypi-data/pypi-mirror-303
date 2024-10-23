from . import Check, Finding
from .utils import is_heading


class HeadingLevelsFinding(Finding):
    NAME = "HeadingLevels"

    def __init__(self, file, line, expected_char, actual_char):
        super().__init__(file, line)
        self.expected_char = expected_char
        self.actual_char = actual_char

    def msg(self):
        return f"Heading must be {self.expected_char} instead of {self.actual_char}"


class HeadingLevelsCheck(Check):
    FINDING = HeadingLevelsFinding

    CONFIG = {"characters": ["=", "-", "+", "~", "^", '"']}

    def __init__(self):
        self.heading_characters = self.CONFIG["characters"]
        super().__init__()
        self.heading_levels = {c: i + 1 for i, c in enumerate(self.heading_characters)}

    def run(self, file, lines):
        current_level = 0
        for i, line in enumerate(lines):
            if is_heading(line):
                if line[0] in self.heading_characters:
                    level = self.heading_levels[line[0]]
                    if level - current_level > 1:
                        self.add_finding(
                            file,
                            i + 1,
                            expected_char=self.heading_characters[current_level],
                            actual_char=line[0],
                        )
                    current_level = level
                else:
                    self.add_finding(
                        file,
                        i + 1,
                        expected_char=self.heading_characters[current_level],
                        actual_char=line[0],
                    )
