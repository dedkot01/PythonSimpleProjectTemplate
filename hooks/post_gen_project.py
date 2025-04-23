import subprocess
from pathlib import Path


def init_git() -> None:
    subprocess.run(["git", "init", "-q"])


def init_venv() -> None:
    command = ["uv", "sync", "-q", "-p", "{{ cookiecutter.python_version }}"]
    if {{ cookiecutter.create_polygon }} is True:
        command += ["--extra", "dev"]
    subprocess.run(command)


def main() -> None:
    if {{ cookiecutter.create_polygon }} is False:
        polygon_file = Path("polygon.ipynb")
        polygon_file.unlink(missing_ok=True)
    if {{ cookiecutter.init_dev_env }} is True:
        init_git()
        init_venv()


if __name__ == "__main__":
    main()
