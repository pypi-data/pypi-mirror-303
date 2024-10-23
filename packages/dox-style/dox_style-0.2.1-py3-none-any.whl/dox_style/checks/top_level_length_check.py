from . import Check, Finding
from .utils import is_index, get_first_heading


class TopLevelLengthFinding(Finding):
    NAME = "TopLevelLength"

    def __init__(self, file, line, exp_length, act_length):
        super().__init__(file, line)
        self._exp_length = exp_length
        self._act_length = act_length

    def msg(self):
        return f"Title too long: {self._act_length} > {self._exp_length}"


class TopLevelLengthCheck(Check):
    FINDING = TopLevelLengthFinding

    CONFIG = {
        "limit": 40,
    }

    def run(self, file, lines):
        if not is_index(file):
            return
        top_level_heading, i = get_first_heading(lines)
        if len(top_level_heading) > self.CONFIG["limit"]:
            self.add_finding(
                file,
                i + 1,
                exp_length=self.CONFIG["limit"],
                act_length=len(top_level_heading),
            )
