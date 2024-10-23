from . import Finding


class Check:
    FINDING = Finding

    CONFIG = {}

    def __init__(self):
        self._findings = []

    @property
    def findings(self):
        return self._findings

    def run(self, file, lines):
        raise NotImplementedError

    def add_finding(self, file, line, **kwargs):
        self._findings.append(self.FINDING(file, line, **kwargs))
