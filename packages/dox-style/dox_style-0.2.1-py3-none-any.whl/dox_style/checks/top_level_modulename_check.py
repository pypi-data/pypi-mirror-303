from . import Check, Finding
from .utils import is_index, get_module, get_first_heading


class TopLevelModuleNameFinding(Finding):
    NAME = "TopLevelModulName"

    def __init__(self, file, line, module_name):
        super().__init__(file, line)
        self.module_name = module_name

    def msg(self):
        return f'Module name "{self.module_name}" not found'


class TopLevelModuleNameCheck(Check):
    FINDING = TopLevelModuleNameFinding

    def run(self, file, lines):
        if not is_index(file):
            return
        module = get_module(file)
        top_level_heading, i = get_first_heading(lines)
        if top_level_heading and not top_level_heading.lower().startswith(module.lower()):
            self.add_finding(file, i + 1, module_name=module)
