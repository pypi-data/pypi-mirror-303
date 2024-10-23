from . import Check, Finding


class DummyFinding(Finding):
    NAME = "DummyFinding"

    def msg(self):
        return "This is some dummy finding message"


class DummyCheck(Check):
    FINDING = DummyFinding

    CONFIG = {
        "some": "config option",
    }

    def run(self, file, lines):
        # file:  path to the document to check
        # lines: content of that document read as list of lines

        # violation found in line 42, add a corresponding finding
        self.add_finding(file, 42)
