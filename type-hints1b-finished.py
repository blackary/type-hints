from pathlib import Path


def get_parent(path: Path) -> Path:
    """Take a path, and return the parent directory"""

    return path.parent


# What if we try to work with the output?

get_parent(Path.cwd()).glob("*")


# Variables:
# not needed in this case, unless you want to make sure you don't
# accidentally reassign x to a different type
x: int = 0
y = 0  # type: int


# Parameters and return types
def fun(y: str) -> bool:
    ...


# class types
def get_path() -> Path:
    ...


def fun1(x: int):
    ...


fun1(1.0)


def fun2(x: float):
    ...


fun2(1)
