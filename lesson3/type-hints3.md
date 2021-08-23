---
marp: true
theme: gaia
---
<!-- class: lead -->

# Python Type Hints, Part 3
#### Python Office Hours 2021-?-?

---
<!-- class: -->

# Topics to Cover

* Overload & Cast
* TYPE_CHECKING
* Mypy settings
* Libraries that take advantage of type hints (FastAPI, Typer, etc.)
* Future of type hints

---
<!-- class: invert -->

# Overload & Cast

```python
from typing import overload

@overload
def halve(value: int) -> float:
    pass
@overload
def halve(value: float) -> float:
    pass
@overload
def halve(value: np.ndarray) -> np.ndarray:
    pass
def halve(value):
    return value / 2

halve(6)[0] # what does mypy say?
halve(np.array([6]))[0]
```

---
# Overload & Cast

`cast` ~ the reverse of `overload`

```python
def get_model_options(model_version: str") -> Dict[str, str]:
    with open(options_path / f"{model_version}.json") as f:
        return json.load(f)
```

What's the problem with this?

---
# TYPE_CHECKING

---
# Mypy Settings

---
# Libaries that use Type Hints

---
# Future of type hints
---

# What did we cover?
<!-- class: -->

* Brief Review
* Callables & Generators
* User-Defined Type Aliases
* Generics
* Overload & Cast
* TYPE_CHECKING
* Mypy settings
* Libraries that take advantage of type hints (FastAPI, Typer, etc.)
* Future of type hints
---

# Future Topics

* Callables & Generators
* User-Defined Types
* Generics
* Overload & Cast
* TYPE_CHECKING
* Mypy settings
* Libraries that take advantage of type hints (FastAPI, Typer, etc.)
* Future of type hints