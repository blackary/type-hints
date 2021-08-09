from pathlib import Path


def get_parent(path: Path) -> Path:
    """Take a path, and return the parent directory"""

    return path.parent


# What if we try to work with the output?

get_parent(Path.cwd()).glob("*")
