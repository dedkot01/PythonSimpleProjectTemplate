from importlib import metadata

try:
    __version__ = metadata.version("{{ cookiecutter.__package_name }}")
except metadata.PackageNotFoundError:
    __version__ = "local"
