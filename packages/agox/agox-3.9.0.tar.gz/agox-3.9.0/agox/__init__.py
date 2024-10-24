import os

# Versioning
__version_info__ = (3, 9, 0)
__version__ = "{}.{}.{}".format(*__version_info__)

# Extra versioning - Mainly for managing Pypi releases.
version_extra = os.environ.get("AGOX_VERSION_EXTRA", None)
if version_extra:
    __version__ = "{}{}".format(__version__, version_extra)

try:  # When installing the package we don't need to actually import.
    from agox.module import Module  # noqa
    from agox.observer import Observer
    from agox.writer import Writer
    from agox.cli.main import main
    from agox.main.state import State
    from agox.main.agox import AGOX

    __all__ = ["Module", "Observer", "Writer", "State", "AGOX", "__version__", "main"]

except ImportError as e:
    print(e)
    pass
