from pathlib import Path


def uppercase(val):
    """Takes a string and upper-cases it"""
    return val.upper()


uppercase("hello")
uppercase(6)


def uppercase_typed(val: str) -> str:
    """Takes a string and upper-cases it"""
    return val.upper()


uppercase_typed("hello")
uppercase_typed(6)


def get_parent(path: Path) -> Path:
    """Take a path, and return the parent directory"""

    
