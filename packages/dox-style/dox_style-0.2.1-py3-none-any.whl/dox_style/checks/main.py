import collections
from copy import deepcopy
from fnmatch import fnmatch
from sphinx.util import logging

from .top_level_casing_check import TopLevelCasingCheck
from .top_level_heading_check import TopLevelHeadingCheck
from .top_level_length_check import TopLevelLengthCheck
from .top_level_modulename_check import TopLevelModuleNameCheck
from .trailing_whitespace_check import TrailingWhitespacesCheck
from .heading_levels_check import HeadingLevelsCheck
from .underline_length_check import UnderlineLengthCheck
from .include_rst_check import IncludeRstCheck

logger = logging.getLogger(__name__)


all_checks = {
    "trailing_whitespaces": TrailingWhitespacesCheck,
    "heading_levels": HeadingLevelsCheck,
    "underline_length": UnderlineLengthCheck,
    "top_level_casing": TopLevelCasingCheck,
    "top_level_heading": TopLevelHeadingCheck,
    "top_level_length": TopLevelLengthCheck,
    "top_level_modulename": TopLevelModuleNameCheck,
    "include_rst": IncludeRstCheck,
}


global_options = {
    "exclude": [],
    "excerpt": 2,
}


common_check_options = {
    "enabled": True,
    "exclude": [],
}


def generate_options():
    options = global_options
    for key, check in all_checks.items():
        options[key] = deepcopy(check.CONFIG)
        options[key].update(common_check_options)

    return options


def updated_options_from_config(config):
    options = generate_options()

    def update(d, u):
        for k, v in u.items():
            if isinstance(v, collections.abc.Mapping):
                d[k] = update(d.get(k, {}), v)
            else:
                d[k] = v
        return d

    update(options, config)

    return options


def style_check(_app, env, docnames):
    options = updated_options_from_config(env.config.stylecheck)

    enabled_checks = []
    for key, check in all_checks.items():
        if options[key]["enabled"]:
            check.CONFIG = deepcopy(options[key])
            enabled_checks.append(check())

    if not enabled_checks:
        logger.warning("No stylechecks enabled")

    for filepath, docname in [(f"{env.srcdir}/{docname}.rst", docname) for docname in docnames]:
        if any([fnmatch(docname, exclusion) for exclusion in options["exclude"]]):
            continue

        try:
            with open(filepath, "r", encoding="utf-8") as file:
                lines = file.read().splitlines()
        except FileNotFoundError:
            logger.error(f"Cannot open {filepath}")
            return

        for check in enabled_checks:
            if any([fnmatch(docname, exclusion) for exclusion in check.CONFIG["exclude"]]):
                continue
            check.run(filepath, lines)

    num_findings = 0
    for check in enabled_checks:
        for finding in check.findings:
            num_findings += 1
            excerpt = env.config.stylecheck.get("excerpt", global_options["excerpt"])
            logger.info(
                f"\n{finding.as_str(show_excerpt=excerpt)}",
                location=(finding.file, finding.line),
                color="red",
            )

    if num_findings > 0:
        logger.warning(f"Found {num_findings} style violations")


def check_setup(app):
    app.connect("env-before-read-docs", style_check)
    app.add_config_value("stylecheck", generate_options(), "env")
