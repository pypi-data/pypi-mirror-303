from .config.main import config_setup
from .checks.main import check_setup
from .version import __version__


def setup(app):
    config_setup(app)
    check_setup(app)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
